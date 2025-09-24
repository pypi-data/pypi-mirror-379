"""
Payment Service - Core payment processing logic.

This service handles universal payment operations, provider orchestration,
and payment lifecycle management.
"""

import logging
from typing import Optional, List
from decimal import Decimal
from datetime import timezone

from django.db import transaction
from django.contrib.auth import get_user_model
from pydantic import BaseModel, Field, ValidationError

from .balance_service import BalanceService
from ...models import UniversalPayment, UserBalance, Transaction
from ...utils.config_utils import get_payments_config
from ..providers.registry import ProviderRegistry
from ..internal_types import (
    ProviderResponse, WebhookData, ServiceOperationResult,
    BalanceUpdateRequest, AccessCheckRequest, AccessCheckResult,
    PaymentCreationResult, WebhookProcessingResult, PaymentStatusResult
)

User = get_user_model()
logger = logging.getLogger(__name__)


class PaymentRequest(BaseModel):
    """Type-safe payment request validation"""
    user_id: int = Field(gt=0, description="User ID")
    amount: Decimal = Field(gt=0, description="Payment amount")
    currency: str = Field(min_length=3, max_length=10, description="Currency code")
    provider: str = Field(min_length=1, description="Payment provider name")
    callback_url: Optional[str] = Field(None, description="Success callback URL")
    cancel_url: Optional[str] = Field(None, description="Cancellation URL")
    metadata: dict = Field(default_factory=dict, description="Additional metadata")


class PaymentResult(BaseModel):
    """Type-safe payment operation result"""
    success: bool
    payment_id: Optional[str] = None
    provider_payment_id: Optional[str] = None
    payment_url: Optional[str] = None
    error_message: Optional[str] = None
    error_code: Optional[str] = None
    metadata: dict = Field(default_factory=dict)


class WebhookProcessingResult(BaseModel):
    """Type-safe webhook processing result"""
    success: bool
    payment_id: Optional[str] = None
    status_updated: bool = False
    balance_updated: bool = False
    error_message: Optional[str] = None


class PaymentService:
    """
    Universal payment processing service.
    
    Handles payment creation, webhook processing, and provider management.
    Integrates with balance management and caching.
    """
    
    def __init__(self):
        """Initialize payment service with dependencies"""
        self.provider_registry = ProviderRegistry()
        self.config = get_payments_config()
    
    def create_payment(self, payment_data: dict) -> 'PaymentCreationResult':
        """
        Create a new payment with the specified provider.
        
        Args:
            payment_data: Dictionary with payment details
            
        Returns:
            PaymentCreationResult with payment details or error information
        """
        try:
            # Validate payment request
            request = PaymentRequest(
                user_id=payment_data['user_id'],
                amount=payment_data['amount'],
                currency=payment_data.get('currency', 'USD'),
                provider=payment_data['provider'],
                metadata=payment_data.get('metadata', {})
            )
            
            # Get provider instance
            provider_instance = self.provider_registry.get_provider(request.provider)
            if not provider_instance:
                return PaymentCreationResult(
                    success=False,
                    error=f"Payment provider '{request.provider}' is not available"
                )
            
            # Get user
            user = User.objects.get(id=request.user_id)
            
            # Convert currency if needed
            amount_usd = self._convert_to_usd(request.amount, request.currency) if request.currency != 'USD' else request.amount
            
            # Create payment record
            with transaction.atomic():
                payment = UniversalPayment.objects.create(
                    user=user,
                    provider=request.provider,
                    amount_usd=amount_usd,
                    currency_code=request.currency,
                    status=UniversalPayment.PaymentStatus.PENDING,
                    metadata=request.metadata
                )
                
                # Prepare provider data
                provider_data = {
                    'amount': float(request.amount),
                    'currency': request.currency,
                    'user_id': user.id,
                    'payment_id': str(payment.id),
                    'callback_url': request.callback_url,
                    'cancel_url': request.cancel_url,
                    **request.metadata
                }
                
                # Process with provider
                provider_result = provider_instance.create_payment(provider_data)
                
                if provider_result.success:
                    # Update payment with provider data
                    payment.provider_payment_id = provider_result.provider_payment_id
                    payment.save()
                    
                    
                    return PaymentCreationResult(
                        success=True,
                        payment_id=str(payment.id),
                        provider_payment_id=provider_result.provider_payment_id,
                        payment_url=provider_result.payment_url
                    )
                else:
                    # Mark payment as failed
                    payment.status = UniversalPayment.PaymentStatus.FAILED
                    payment.error_message = provider_result.error_message or 'Unknown provider error'
                    payment.save()
                    
                    return PaymentCreationResult(
                        success=False,
                        payment_id=str(payment.id),
                        error=provider_result.error_message or 'Payment creation failed'
                    )
                    
        except ValidationError as e:
            logger.error(f"Payment validation error: {e}")
            return PaymentCreationResult(
                success=False,
                error=f"Invalid payment data: {e}"
            )
        except Exception as e:
            logger.error(f"Payment creation failed: {e}", exc_info=True)
            return PaymentCreationResult(
                success=False,
                error=f"Internal error: {str(e)}"
            )
    
    def process_webhook(
        self,
        provider: str,
        webhook_data: dict,
        request_headers: Optional[dict] = None
    ) -> 'WebhookProcessingResult':
        """
        Process payment webhook from provider.
        
        Args:
            provider: Payment provider name
            webhook_data: Webhook payload data
            request_headers: HTTP headers for validation
            
        Returns:
            WebhookProcessingResult with processing status
        """
        try:
            # Get provider instance
            provider_instance = self.provider_registry.get_provider(provider)
            if not provider_instance:
                return WebhookProcessingResult(
                    success=False,
                    error=f"Provider '{provider}' not found"
                )
            
            # Process webhook with provider
            webhook_result = provider_instance.process_webhook(webhook_data)
            if not webhook_result.success:
                return WebhookProcessingResult(
                    success=False,
                    error=webhook_result.error_message or "Webhook processing failed"
                )
            
            # Find payment by provider payment ID
            try:
                payment = UniversalPayment.objects.get(
                    provider_payment_id=webhook_result.provider_payment_id
                )
            except UniversalPayment.DoesNotExist:
                return WebhookProcessingResult(
                    success=False,
                    error=f"Payment not found: {webhook_result.provider_payment_id}"
                )
            
            # Process payment status update
            old_status = payment.status
            new_status = webhook_result.status
            
            with transaction.atomic():
                # Update payment
                payment.status = new_status
                payment.save()
                
                # Process completion if status changed to completed
                balance_updated = False
                if (new_status == UniversalPayment.PaymentStatus.COMPLETED and 
                    old_status != UniversalPayment.PaymentStatus.COMPLETED):
                    balance_updated = self._process_payment_completion(payment)
                
                
                return WebhookProcessingResult(
                    success=True,
                    payment_id=str(payment.id),
                    status_updated=(old_status != new_status),
                    balance_updated=balance_updated
                )
                
        except Exception as e:
            logger.error(f"Webhook processing failed for {provider}: {e}", exc_info=True)
            return WebhookProcessingResult(
                success=False,
                error=f"Webhook processing error: {str(e)}"
            )
    
    def get_payment_status(self, payment_id: str) -> Optional['PaymentStatusResult']:
        """
        Get payment status by ID.
        
        Args:
            payment_id: Payment UUID
            
        Returns:
            Payment status information or None if not found
        """
        try:
            
            # Get from database
            payment = UniversalPayment.objects.get(id=payment_id)
            
            return PaymentStatusResult(
                payment_id=str(payment.id),
                status=payment.status,
                amount_usd=payment.amount_usd,
                currency_code=payment.currency_code,
                provider=payment.provider,
                provider_payment_id=payment.provider_payment_id,
                created_at=payment.created_at,
                updated_at=payment.updated_at
            )
            
        except UniversalPayment.DoesNotExist:
            return None
        except Exception as e:
            logger.error(f"Error getting payment status {payment_id}: {e}")
            return None
    
    def get_user_payments(
        self,
        user: User,
        status: Optional[str] = None,
        limit: int = 50,
        offset: int = 0
    ) -> List[dict]:
        """
        Get user's payment history.
        
        Args:
            user: User object
            status: Filter by payment status
            limit: Number of payments to return
            offset: Pagination offset
            
        Returns:
            List of payment dictionaries
        """
        try:
            queryset = UniversalPayment.objects.filter(user=user)
            
            if status:
                queryset = queryset.filter(status=status)
            
            payments = queryset.order_by('-created_at')[offset:offset+limit]
            
            return [
                {
                    'id': str(payment.id),
                    'status': payment.status,
                    'amount_usd': str(payment.amount_usd),
                    'pay_amount': str(payment.pay_amount) if payment.pay_amount else str(payment.amount_usd),
                    'currency_code': payment.currency_code,
                    'provider': payment.provider.name if payment.provider else None,
                    'created_at': payment.created_at.isoformat(),
                    'processed_at': payment.processed_at.isoformat() if payment.processed_at else None
                }
                for payment in payments
            ]
            
        except Exception as e:
            logger.error(f"Error getting user payments for {user.id}: {e}")
            return []
    
    def _process_payment_completion(self, payment: UniversalPayment) -> bool:
        """
        Process completed payment by adding funds to user balance.
        
        Args:
            payment: Completed payment object
            
        Returns:
            True if balance was updated, False otherwise
        """
        try:
            
            balance_service = BalanceService()
            result = balance_service.add_funds(
                user=payment.user,
                amount=payment.amount_usd,
                currency_code='USD',
                source='payment',
                reference_id=str(payment.id),
                metadata={
                    'provider': payment.provider.name if payment.provider else 'unknown',
                    'provider_payment_id': payment.provider_payment_id,
                    'pay_amount': str(payment.pay_amount) if payment.pay_amount else str(payment.amount_usd),
                    'currency_code': payment.currency_code
                }
            )
            
            
            return result.success
            
        except Exception as e:
            logger.error(f"Error processing payment completion {payment.id}: {e}")
            return False
    
    def _convert_to_usd(self, amount: Decimal, currency: str) -> Decimal:
        """
        Convert amount to USD using current exchange rates.
        
        Args:
            amount: Amount to convert
            currency: Source currency
            
        Returns:
            Amount in USD
        """
        if currency == 'USD':
            return amount
        
        # TODO: Implement currency conversion using exchange rate API
        # For now, return the same amount (assuming USD)
        logger.warning(f"Currency conversion not implemented for {currency}, using 1:1 rate")
        return amount
    
    
    def list_available_providers(self) -> List[dict]:
        """
        List all available payment providers.
        
        Returns:
            List of provider information
        """
        return [
            {
                'name': name,
                'display_name': provider.get_display_name(),
                'supported_currencies': provider.get_supported_currencies(),
                'is_active': provider.is_active(),
                'provider_type': provider.get_provider_type()
            }
            for name, provider in self.provider_registry.get_all_providers().items()
        ]
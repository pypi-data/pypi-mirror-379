"""
Payment models for the universal payments system.
"""

from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from .base import TimestampedModel

User = get_user_model()



class UniversalPayment(TimestampedModel):
    """Universal payment model for all providers."""
    
    class PaymentStatus(models.TextChoices):
        PENDING = "pending", "Pending"
        CONFIRMING = "confirming", "Confirming"
        CONFIRMED = "confirmed", "Confirmed"
        COMPLETED = "completed", "Completed"
        FAILED = "failed", "Failed"
        EXPIRED = "expired", "Expired"
        CANCELLED = "cancelled", "Cancelled"
        REFUNDED = "refunded", "Refunded"
    
    class PaymentProvider(models.TextChoices):
        NOWPAYMENTS = "nowpayments", "NowPayments"
        STRIPE = "stripe", "Stripe"
        INTERNAL = "internal", "Internal"
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='universal_payments',
        help_text="User who initiated this payment"
    )
    
    # Financial data
    amount_usd = models.FloatField(
        validators=[MinValueValidator(1.0)],
        help_text="Payment amount in USD"
    )
    currency_code = models.CharField(
        max_length=10,
        help_text="Currency used for payment"
    )
    
    # Actual received amount (may differ from requested)
    actual_amount_usd = models.FloatField(
        null=True,
        blank=True,
        help_text="Actual received amount in USD"
    )
    actual_currency_code = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        help_text="Actual received currency"
    )
    
    # Fee information
    fee_amount_usd = models.FloatField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0.0)],
        help_text="Fee amount in USD"
    )
    
    # Payment details
    provider = models.CharField(
        max_length=50,
        choices=PaymentProvider.choices,
        help_text="Payment provider"
    )
    status = models.CharField(
        max_length=20,
        choices=PaymentStatus.choices,
        default=PaymentStatus.PENDING,
        help_text="Payment status"
    )
    
    # Provider-specific fields
    provider_payment_id = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        unique=True,
        help_text="Provider's payment ID"
    )
    internal_payment_id = models.CharField(
        max_length=100,
        unique=True,
        help_text="Internal payment identifier"
    )
    
    # Crypto payment specific
    pay_address = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text="Cryptocurrency payment address"
    )
    pay_amount = models.FloatField(
        null=True,
        blank=True,
        help_text="Amount to pay in cryptocurrency"
    )
    network = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text="Blockchain network (mainnet, testnet, etc.)"
    )
    
    # Metadata
    description = models.TextField(
        blank=True,
        help_text="Payment description"
    )
    order_id = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Order reference ID"
    )
    metadata = models.JSONField(
        default=dict,
        help_text="Additional metadata"
    )
    
    # Provider webhook data
    webhook_data = models.JSONField(
        null=True,
        blank=True,
        help_text="Raw webhook data from provider"
    )
    
    # Timestamps
    expires_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Payment expiration time"
    )
    completed_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Payment completion time"
    )
    processed_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="When the payment was processed and funds added to balance"
    )

    # Import and assign manager
    from ..managers import UniversalPaymentManager
    objects = UniversalPaymentManager()

    class Meta:
        db_table = 'universal_payments'
        verbose_name = "Universal Payment"
        verbose_name_plural = "Universal Payments"
        indexes = [
            models.Index(fields=['user', 'status']),
            models.Index(fields=['provider_payment_id']),
            models.Index(fields=['internal_payment_id']),
            models.Index(fields=['status']),
            models.Index(fields=['provider']),
            models.Index(fields=['currency_code']),
            models.Index(fields=['created_at']),
            models.Index(fields=['processed_at']),
        ]
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.email} - ${self.amount_usd} ({self.currency_code}) - {self.get_status_display()}"

    @property
    def is_pending(self) -> bool:
        """Check if payment is still pending."""
        return self.status in [
            self.PaymentStatus.PENDING,
            self.PaymentStatus.CONFIRMING,
            self.PaymentStatus.CONFIRMED
        ]

    @property
    def is_completed(self) -> bool:
        """Check if payment is completed."""
        return self.status == self.PaymentStatus.COMPLETED

    @property
    def is_failed(self) -> bool:
        """Check if payment failed."""
        return self.status in [self.PaymentStatus.FAILED, self.PaymentStatus.EXPIRED]

    @property
    def needs_processing(self) -> bool:
        """Check if payment needs to be processed (completed but not processed)."""
        return self.is_completed and not self.processed_at

    @property
    def is_crypto_payment(self) -> bool:
        """Check if this is a cryptocurrency payment."""
        return self.provider == self.PaymentProvider.NOWPAYMENTS

    def get_payment_url(self) -> str:
        """Get payment URL for QR code or direct payment."""
        if self.pay_address and self.pay_amount:
            return f"{self.currency_code.lower()}:{self.pay_address}?amount={self.pay_amount}"
        return ""

    def get_qr_code_url(self, size: int = 200) -> str:
        """Get QR code URL for payment."""
        payment_url = self.get_payment_url()
        if payment_url:
            return f"https://api.qrserver.com/v1/create-qr-code/?size={size}x{size}&data={payment_url}"
        return ""

    def mark_as_processed(self):
        """Mark payment as processed."""
        if not self.processed_at:
            self.processed_at = timezone.now()
            self.save(update_fields=['processed_at'])

    def update_from_webhook(self, webhook_data: dict):
        """Update payment from provider webhook data."""
        self.webhook_data = webhook_data
        
        # Update status if provided
        if 'payment_status' in webhook_data:
            self.status = webhook_data['payment_status']
        
        # Update payment details if provided
        if 'pay_address' in webhook_data:
            self.pay_address = webhook_data['pay_address']
        
        if 'pay_amount' in webhook_data:
            self.pay_amount = float(str(webhook_data['pay_amount']))
        
        if 'payment_id' in webhook_data:
            self.provider_payment_id = webhook_data['payment_id']
        
        self.save()

    def can_be_refunded(self) -> bool:
        """Check if payment can be refunded."""
        return self.is_completed and self.processed_at

    def get_currency_display_name(self) -> str:
        """Get human-readable currency name."""
        # This could be enhanced to lookup from Currency model
        currency_names = {
            'BTC': 'Bitcoin',
            'ETH': 'Ethereum',
            'USD': 'US Dollar',
            'EUR': 'Euro',
        }
        return currency_names.get(self.currency_code, self.currency_code)

    def get_status_color(self) -> str:
        """Get color for status display."""
        status_colors = {
            self.PaymentStatus.PENDING: '#6c757d',
            self.PaymentStatus.CONFIRMING: '#fd7e14',
            self.PaymentStatus.CONFIRMED: '#20c997',
            self.PaymentStatus.COMPLETED: '#198754',
            self.PaymentStatus.FAILED: '#dc3545',
            self.PaymentStatus.REFUNDED: '#6f42c1',
            self.PaymentStatus.EXPIRED: '#dc3545',
            self.PaymentStatus.CANCELLED: '#6c757d'
        }
        return status_colors.get(self.status, '#6c757d')

    def clean(self):
        """Validate payment data."""
        
        # Validate minimum amount
        if self.amount_usd < 1.0:
            raise ValidationError("Minimum payment amount is $1.00")
        
        # Validate crypto address for crypto payments
        if self.is_crypto_payment and self.status != self.PaymentStatus.PENDING:
            if not self.pay_address:
                raise ValidationError("Payment address is required for crypto payments")

    def save(self, *args, **kwargs):
        """Override save to run validation."""
        if self.currency_code:
            self.currency_code = self.currency_code.upper()
        
        # Generate internal payment ID if not set
        if not self.internal_payment_id:
            import uuid
            self.internal_payment_id = f"pay_{str(uuid.uuid4())[:8]}"
        
        self.clean()
        super().save(*args, **kwargs)

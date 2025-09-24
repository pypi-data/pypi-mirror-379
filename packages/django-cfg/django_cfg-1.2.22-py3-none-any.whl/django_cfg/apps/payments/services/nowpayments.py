"""
NowPayments provider implementation.
"""

from typing import Dict, Any
from decimal import Decimal
import requests
from .base import PaymentProvider


class NowPaymentsProvider(PaymentProvider):
    """NowPayments crypto payment provider."""
    
    def __init__(self, config: Dict[str, Any]):
        """Initialize NowPayments provider."""
        super().__init__(config)
        self.api_key = config.get('api_key')
        self.base_url = config.get('base_url', 'https://api.nowpayments.io/v1')
        self.headers = {'x-api-key': self.api_key}
    
    def create_payment(self, amount: Decimal, currency: str, **kwargs) -> Dict[str, Any]:
        """Create payment via NowPayments API."""
        payload = {
            'price_amount': float(amount),
            'price_currency': 'USD',
            'pay_currency': currency.upper(),
            'order_id': kwargs.get('order_id'),
            'order_description': kwargs.get('description', 'Payment'),
            'ipn_callback_url': kwargs.get('callback_url'),
            'success_url': kwargs.get('success_url'),
            'cancel_url': kwargs.get('cancel_url'),
        }
        
        response = requests.post(
            f"{self.base_url}/payment",
            json=payload,
            headers=self.headers,
            timeout=30
        )
        response.raise_for_status()
        return response.json()
    
    def check_payment_status(self, payment_id: str) -> Dict[str, Any]:
        """Check payment status via NowPayments API."""
        response = requests.get(
            f"{self.base_url}/payment/{payment_id}",
            headers=self.headers,
            timeout=30
        )
        response.raise_for_status()
        return response.json()
    
    def process_webhook(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Process NowPayments webhook."""
        # Extract important fields from webhook
        return {
            'payment_id': payload.get('payment_id'),
            'payment_status': payload.get('payment_status'),
            'pay_address': payload.get('pay_address'),
            'pay_amount': payload.get('pay_amount'),
            'pay_currency': payload.get('pay_currency'),
            'price_amount': payload.get('price_amount'),
            'price_currency': payload.get('price_currency'),
            'order_id': payload.get('order_id'),
            'outcome_amount': payload.get('outcome_amount'),
            'outcome_currency': payload.get('outcome_currency'),
        }
    
    def get_supported_currencies(self) -> list[str]:
        """Get supported cryptocurrencies from NowPayments."""
        response = requests.get(
            f"{self.base_url}/currencies",
            headers=self.headers,
            timeout=30
        )
        response.raise_for_status()
        data = response.json()
        return data.get('currencies', [])

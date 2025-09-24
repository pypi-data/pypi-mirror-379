"""
Payment provider configurations.

Defines configuration classes for different payment providers.
"""

from typing import Dict, Any, Optional
from pydantic import BaseModel, Field, SecretStr


class PaymentProviderConfig(BaseModel):
    """Base configuration for payment providers."""
    enabled: bool = True
    sandbox: bool = Field(default=True, description="Use sandbox mode")
    api_key: SecretStr = Field(description="Provider API key")
    timeout: int = Field(default=30, description="Request timeout in seconds")
    max_retries: int = Field(default=3, description="Maximum retry attempts")
    
    def get_config_dict(self) -> Dict[str, Any]:
        """Get configuration as dictionary for provider initialization."""
        return {
            'api_key': self.api_key.get_secret_value(),
            'sandbox': self.sandbox,
            'timeout': self.timeout,
            'max_retries': self.max_retries
        }


class NowPaymentsConfig(PaymentProviderConfig):
    """NowPayments provider configuration."""
    public_key: Optional[SecretStr] = Field(default=None, description="NowPayments public key")
    callback_url: Optional[str] = Field(default=None, description="Webhook callback URL")
    success_url: Optional[str] = Field(default=None, description="Payment success URL")
    cancel_url: Optional[str] = Field(default=None, description="Payment cancel URL")
    
    def get_config_dict(self) -> Dict[str, Any]:
        """Get configuration as dictionary for provider initialization."""
        config = super().get_config_dict()
        config.update({
            'callback_url': self.callback_url,
            'success_url': self.success_url,
            'cancel_url': self.cancel_url,
        })
        return config


class StripeConfig(PaymentProviderConfig):
    """Stripe provider configuration."""
    publishable_key: Optional[SecretStr] = Field(default=None, description="Stripe publishable key")
    webhook_secret: Optional[SecretStr] = Field(default=None, description="Stripe webhook secret")
    
    def get_config_dict(self) -> Dict[str, Any]:
        """Get configuration as dictionary for provider initialization."""
        config = super().get_config_dict()
        config.update({
            'publishable_key': self.publishable_key.get_secret_value() if self.publishable_key else None,
            'webhook_secret': self.webhook_secret.get_secret_value() if self.webhook_secret else None,
        })
        return config


class CryptAPIConfig(PaymentProviderConfig):
    """CryptAPI provider configuration."""
    own_address: str = Field(description="Your crypto address where funds will be sent")
    callback_url: Optional[str] = Field(default=None, description="Webhook callback URL")
    convert_payments: bool = Field(default=True, description="Auto-convert payments to your address currency")
    multi_token: bool = Field(default=True, description="Enable multi-token support")
    priority: str = Field(default='default', description="Transaction priority (default, economic, priority)")
    
    def get_config_dict(self) -> Dict[str, Any]:
        """Get configuration as dictionary for provider initialization."""
        config = super().get_config_dict()
        config.update({
            'own_address': self.own_address,
            'callback_url': self.callback_url,
            'convert_payments': self.convert_payments,
            'multi_token': self.multi_token,
            'priority': self.priority,
        })
        return config


# Provider registry for easy access
PROVIDER_CONFIGS = {
    'nowpayments': NowPaymentsConfig,
    'stripe': StripeConfig,
    'cryptapi': CryptAPIConfig,
}


def get_provider_config_class(provider_name: str) -> Optional[type]:
    """Get provider configuration class by name."""
    return PROVIDER_CONFIGS.get(provider_name)

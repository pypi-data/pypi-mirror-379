"""
Payment configuration module.

Handles loading and managing payment configurations from project settings.
"""

from typing import Optional
from pydantic import SecretStr
import logging

from django_cfg.modules.base import BaseCfgModule
from .settings import PaymentsSettings
from .providers import NowPaymentsConfig, StripeConfig, CryptAPIConfig, get_provider_config_class

logger = logging.getLogger(__name__)


class PaymentsCfgModule(BaseCfgModule):
    """Payment configuration module for django-cfg."""
    
    def __init__(self):
        super().__init__()
        self.settings_class = PaymentsSettings
        self._settings_cache = None
    
    def get_config(self) -> PaymentsSettings:
        """Get payments configuration."""
        if self._settings_cache is None:
            project_config = super().get_config()
            if project_config:
                self._settings_cache = self.load_from_project_config(project_config)
            else:
                self._settings_cache = PaymentsSettings()
        return self._settings_cache
    
    def reset_cache(self):
        """Reset configuration cache."""
        self._settings_cache = None
    
    def load_from_project_config(self, config) -> PaymentsSettings:
        """Load payments configuration from main project config."""
        # Get base settings
        settings_dict = {}
        
        # Load from django-cfg config if available
        if hasattr(config, 'enable_payments'):
            settings_dict['enabled'] = config.enable_payments
        
        if hasattr(config, 'debug'):
            settings_dict['debug_mode'] = config.debug
        
        # Load provider configurations from environment/config
        providers = {}
        
        # Load NowPayments configuration
        if self._has_provider_config(config, 'nowpayments'):
            nowpayments_config = self._get_provider_config(config, 'nowpayments')
            if nowpayments_config:
                providers['nowpayments'] = nowpayments_config
        
        # Load Stripe configuration
        if self._has_provider_config(config, 'stripe'):
            stripe_config = self._get_provider_config(config, 'stripe')
            if stripe_config:
                providers['stripe'] = stripe_config
        
        # Load CryptAPI configuration
        if self._has_provider_config(config, 'cryptapi'):
            cryptapi_config = self._get_provider_config(config, 'cryptapi')
            if cryptapi_config:
                providers['cryptapi'] = cryptapi_config
        
        
        settings_dict['providers'] = providers
        
        return PaymentsSettings(**settings_dict)
    
    def _has_provider_config(self, config, provider_name: str) -> bool:
        """Check if provider configuration exists."""
        return (
            hasattr(config, 'api_keys') and 
            hasattr(config.api_keys, provider_name)
        )
    
    def _get_provider_config(self, config, provider_name: str) -> Optional[object]:
        """Get provider configuration."""
        try:
            if provider_name == 'nowpayments':
                return self._load_nowpayments_config(config)
            elif provider_name == 'stripe':
                return self._load_stripe_config(config)
            elif provider_name == 'cryptapi':
                return self._load_cryptapi_config(config)
            else:
                logger.warning(f"Unknown provider: {provider_name}")
                return None
        except Exception as e:
            logger.error(f"Error loading {provider_name} config: {e}")
            return None
    
    def _load_nowpayments_config(self, config) -> Optional[NowPaymentsConfig]:
        """Load NowPayments configuration."""
        nowpayments_config = config.api_keys.nowpayments
        if not hasattr(nowpayments_config, 'api_key'):
            return None
        
        return NowPaymentsConfig(
            api_key=SecretStr(nowpayments_config.api_key),
            public_key=SecretStr(nowpayments_config.public_key) if hasattr(nowpayments_config, 'public_key') else None,
            sandbox=getattr(config, 'debug', True),
            callback_url=self._build_callback_url(config, 'nowpayments'),
            success_url=self._build_success_url(config),
            cancel_url=self._build_cancel_url(config)
        )
    
    def _load_stripe_config(self, config) -> Optional[StripeConfig]:
        """Load Stripe configuration."""
        stripe_config = config.api_keys.stripe
        if not hasattr(stripe_config, 'secret_key'):
            return None
        
        return StripeConfig(
            api_key=SecretStr(stripe_config.secret_key),
            publishable_key=SecretStr(stripe_config.publishable_key) if hasattr(stripe_config, 'publishable_key') else None,
            webhook_secret=SecretStr(stripe_config.webhook_secret) if hasattr(stripe_config, 'webhook_secret') else None,
            sandbox=getattr(config, 'debug', True)
        )
    
    def _load_cryptapi_config(self, config) -> Optional[CryptAPIConfig]:
        """Load CryptAPI configuration."""
        cryptapi_config = config.api_keys.cryptapi
        if not hasattr(cryptapi_config, 'own_address'):
            return None
        
        return CryptAPIConfig(
            api_key=SecretStr('dummy'),  # CryptAPI doesn't require API key
            own_address=cryptapi_config.own_address,
            callback_url=self._build_callback_url(config, 'cryptapi'),
            convert_payments=getattr(cryptapi_config, 'convert_payments', True),
            multi_token=getattr(cryptapi_config, 'multi_token', True),
            priority=getattr(cryptapi_config, 'priority', 'default'),
            sandbox=getattr(config, 'debug', True)
        )
    
    
    def _build_callback_url(self, config, provider: str) -> Optional[str]:
        """Build webhook callback URL for provider."""
        if hasattr(config, 'api_url') and config.api_url:
            return f"{config.api_url}/api/payments/webhook/{provider}/"
        return None
    
    def _build_success_url(self, config) -> Optional[str]:
        """Build payment success URL."""
        if hasattr(config, 'site_url') and config.site_url:
            return f"{config.site_url}/payments/success/"
        return None
    
    def _build_cancel_url(self, config) -> Optional[str]:
        """Build payment cancel URL."""
        if hasattr(config, 'site_url') and config.site_url:
            return f"{config.site_url}/payments/cancel/"
        return None

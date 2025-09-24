"""
Configuration utility functions.

Helper functions for working with payment configurations.
"""

from typing import Optional, List, Dict, Any
import logging

from .module import PaymentsCfgModule
from .settings import PaymentsSettings
from .providers import PaymentProviderConfig, NowPaymentsConfig, StripeConfig, CryptAPIConfig

logger = logging.getLogger(__name__)

# Global payments configuration instance
_payments_config = PaymentsCfgModule()


def get_payments_config() -> PaymentsSettings:
    """Get current payments configuration."""
    return _payments_config.get_config()


def get_provider_config(provider_name: str) -> Optional[PaymentProviderConfig]:
    """Get configuration for specific payment provider."""
    config = get_payments_config()
    return config.providers.get(provider_name)


def get_nowpayments_config() -> Optional[NowPaymentsConfig]:
    """Get NowPayments configuration."""
    provider_config = get_provider_config('nowpayments')
    if isinstance(provider_config, NowPaymentsConfig):
        return provider_config
    return None


def get_stripe_config() -> Optional[StripeConfig]:
    """Get Stripe configuration."""
    provider_config = get_provider_config('stripe')
    if isinstance(provider_config, StripeConfig):
        return provider_config
    return None


def get_cryptapi_config() -> Optional[CryptAPIConfig]:
    """Get CryptAPI configuration."""
    provider_config = get_provider_config('cryptapi')
    if isinstance(provider_config, CryptAPIConfig):
        return provider_config
    return None




def is_payments_enabled() -> bool:
    """Check if payments module is enabled."""
    try:
        config = get_payments_config()
        return config.enabled
    except Exception as e:
        logger.warning(f"Error checking payments status: {e}")
        return False


def is_feature_enabled(feature_name: str) -> bool:
    """Check if specific payment feature is enabled."""
    try:
        config = get_payments_config()
        feature_map = {
            'crypto_payments': config.enable_crypto_payments,
            'fiat_payments': config.enable_fiat_payments,
            'subscriptions': config.enable_subscription_system,
            'balance': config.enable_balance_system,
            'api_keys': config.enable_api_key_system,
            'webhooks': config.enable_webhook_processing,
        }
        return feature_map.get(feature_name, False)
    except Exception as e:
        logger.warning(f"Error checking feature {feature_name}: {e}")
        return False


def get_enabled_providers() -> List[str]:
    """Get list of enabled payment providers."""
    try:
        config = get_payments_config()
        return [name for name, provider_config in config.providers.items() if provider_config.enabled]
    except Exception as e:
        logger.warning(f"Error getting enabled providers: {e}")
        return []


def get_provider_settings(provider_name: str) -> Dict[str, Any]:
    """Get provider settings as dictionary for service initialization."""
    try:
        provider_config = get_provider_config(provider_name)
        if provider_config:
            return provider_config.get_config_dict()
        return {}
    except Exception as e:
        logger.error(f"Error getting settings for provider {provider_name}: {e}")
        return {}


def validate_provider_config(provider_name: str) -> bool:
    """Validate provider configuration."""
    try:
        provider_config = get_provider_config(provider_name)
        if not provider_config:
            return False
        
        # Basic validation - check if API key exists
        config_dict = provider_config.get_config_dict()
        return bool(config_dict.get('api_key'))
        
    except Exception as e:
        logger.error(f"Error validating provider {provider_name}: {e}")
        return False


def get_rate_limit_settings() -> Dict[str, int]:
    """Get rate limiting settings."""
    try:
        config = get_payments_config()
        return {
            'hourly_limit': config.rate_limits.default_rate_limit_per_hour,
            'daily_limit': config.rate_limits.default_rate_limit_per_day,
            'burst_multiplier': config.rate_limits.burst_limit_multiplier,
            'window_size': config.rate_limits.sliding_window_size,
        }
    except Exception as e:
        logger.warning(f"Error getting rate limit settings: {e}")
        return {
            'hourly_limit': 1000,
            'daily_limit': 10000,
            'burst_multiplier': 2.0,
            'window_size': 3600,
        }


def get_cache_settings() -> Dict[str, int]:
    """Get cache timeout settings."""
    try:
        config = get_payments_config()
        return {
            'access_check': config.cache.cache_timeout_access_check,
            'user_balance': config.cache.cache_timeout_user_balance,
            'subscriptions': config.cache.cache_timeout_subscriptions,
            'provider_status': config.cache.cache_timeout_provider_status,
            'currency_rates': config.cache.cache_timeout_currency_rates,
        }
    except Exception as e:
        logger.warning(f"Error getting cache settings: {e}")
        return {
            'access_check': 60,
            'user_balance': 300,
            'subscriptions': 600,
            'provider_status': 1800,
            'currency_rates': 3600,
        }


def get_billing_settings() -> Dict[str, Any]:
    """Get billing settings."""
    try:
        config = get_payments_config()
        return {
            'auto_bill': config.billing.auto_bill_subscriptions,
            'grace_period_hours': config.billing.billing_grace_period_hours,
            'retry_failed': config.billing.retry_failed_payments,
            'max_retries': config.billing.max_payment_retries,
            'min_amount_usd': config.billing.min_payment_amount_usd,
            'max_amount_usd': config.billing.max_payment_amount_usd,
        }
    except Exception as e:
        logger.warning(f"Error getting billing settings: {e}")
        return {
            'auto_bill': True,
            'grace_period_hours': 24,
            'retry_failed': True,
            'max_retries': 3,
            'min_amount_usd': 1.0,
            'max_amount_usd': 50000.0,
        }


def reset_config_cache():
    """Reset configuration cache (useful for testing)."""
    global _payments_config
    _payments_config.reset_cache()


def reload_config():
    """Reload configuration from project settings."""
    reset_config_cache()
    return get_payments_config()

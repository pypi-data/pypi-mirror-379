"""
Universal Payment Configuration.

Modular configuration system for the payments module.
"""

# Core configuration classes
from .settings import (
    PaymentsSettings,
    SecuritySettings,
    RateLimitSettings,
    BillingSettings,
    CacheSettings,
    NotificationSettings
)

# Provider configurations
from .providers import (
    PaymentProviderConfig,
    NowPaymentsConfig,
    StripeConfig,
    CryptAPIConfig,
    get_provider_config_class,
    PROVIDER_CONFIGS
)

# Configuration module
from .module import PaymentsCfgModule

# Utility functions
from .utils import (
    get_payments_config,
    get_provider_config,
    get_nowpayments_config,
    get_stripe_config,
    is_payments_enabled,
    is_feature_enabled,
    get_enabled_providers,
    get_provider_settings,
    validate_provider_config,
    get_rate_limit_settings,
    get_cache_settings,
    get_billing_settings,
    reset_config_cache,
    reload_config
)

# Backwards compatibility exports
payments_config = PaymentsCfgModule()

__all__ = [
    # Core settings
    'PaymentsSettings',
    'SecuritySettings',
    'RateLimitSettings',
    'BillingSettings',
    'CacheSettings',
    'NotificationSettings',
    
    # Provider configurations
    'PaymentProviderConfig',
    'NowPaymentsConfig',
    'StripeConfig',
    'CryptAPIConfig',
    'get_provider_config_class',
    'PROVIDER_CONFIGS',
    
    # Configuration module
    'PaymentsCfgModule',
    'payments_config',
    
    # Utility functions
    'get_payments_config',
    'get_provider_config',
    'get_nowpayments_config',
    'get_stripe_config',
    'is_payments_enabled',
    'is_feature_enabled',
    'get_enabled_providers',
    'get_provider_settings',
    'validate_provider_config',
    'get_rate_limit_settings',
    'get_cache_settings',
    'get_billing_settings',
    'reset_config_cache',
    'reload_config',
]

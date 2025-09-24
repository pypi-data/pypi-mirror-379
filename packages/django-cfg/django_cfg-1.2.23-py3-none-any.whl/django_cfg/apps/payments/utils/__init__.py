"""
Utilities for universal payments.
"""

from .middleware_utils import get_client_ip, is_api_request, extract_api_key
# from .billing_utils import calculate_usage_cost, create_billing_transaction  # TODO: Implement when needed
from .validation_utils import validate_api_key, check_subscription_access

# Configuration utilities
from .config_utils import (
    PaymentsConfigUtil,
    RedisConfigHelper,
    CacheConfigHelper, 
    ProviderConfigHelper,
    get_payments_config,
    is_payments_enabled,
    is_debug_mode
)

__all__ = [
    # Middleware utilities
    'get_client_ip',
    'is_api_request', 
    'extract_api_key',
    
    # Billing utilities (TODO: Implement when needed)
    # 'calculate_usage_cost',
    # 'create_billing_transaction',
    
    # Validation utilities
    'validate_api_key',
    'check_subscription_access',
    
    # Configuration utilities
    'PaymentsConfigUtil',
    'RedisConfigHelper',
    'CacheConfigHelper',
    'ProviderConfigHelper', 
    'get_payments_config',
    'is_payments_enabled',
    'is_debug_mode',
]

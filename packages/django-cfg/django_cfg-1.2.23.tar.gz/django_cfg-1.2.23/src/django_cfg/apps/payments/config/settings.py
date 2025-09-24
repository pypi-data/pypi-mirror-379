"""
Universal payments module settings.

Core settings for the payments system including security, rate limiting, billing, etc.
"""

from typing import Dict
from pydantic import BaseModel, Field

from .providers import PaymentProviderConfig


class SecuritySettings(BaseModel):
    """Security-related payment settings."""
    api_key_length: int = Field(default=32, description="API key length in characters")
    api_key_prefix: str = Field(default="ak_", description="API key prefix")
    min_balance_threshold: float = Field(default=0.0, description="Minimum balance threshold")
    auto_create_api_keys: bool = Field(default=True, description="Auto-create API keys for new users")


class RateLimitSettings(BaseModel):
    """Rate limiting settings."""
    default_rate_limit_per_hour: int = Field(default=1000, description="Default API rate limit per hour")
    default_rate_limit_per_day: int = Field(default=10000, description="Default API rate limit per day")
    burst_limit_multiplier: float = Field(default=2.0, description="Burst limit multiplier")
    sliding_window_size: int = Field(default=3600, description="Sliding window size in seconds")


class BillingSettings(BaseModel):
    """Billing and subscription settings."""
    auto_bill_subscriptions: bool = Field(default=True, description="Automatically bill subscriptions")
    billing_grace_period_hours: int = Field(default=24, description="Grace period for failed billing")
    retry_failed_payments: bool = Field(default=True, description="Retry failed payments")
    max_payment_retries: int = Field(default=3, description="Maximum payment retry attempts")
    min_payment_amount_usd: float = Field(default=1.0, description="Minimum payment amount in USD")
    max_payment_amount_usd: float = Field(default=50000.0, description="Maximum payment amount in USD")


class CacheSettings(BaseModel):
    """Cache timeout settings."""
    cache_timeout_access_check: int = Field(default=60, description="Cache timeout for access checks (seconds)")
    cache_timeout_user_balance: int = Field(default=300, description="Cache timeout for user balance (seconds)")
    cache_timeout_subscriptions: int = Field(default=600, description="Cache timeout for subscriptions (seconds)")
    cache_timeout_provider_status: int = Field(default=1800, description="Cache timeout for provider status (seconds)")
    cache_timeout_currency_rates: int = Field(default=3600, description="Cache timeout for currency rates (seconds)")


class NotificationSettings(BaseModel):
    """Notification settings."""
    send_payment_confirmations: bool = Field(default=True, description="Send payment confirmation emails")
    send_subscription_renewals: bool = Field(default=True, description="Send subscription renewal notifications")
    send_balance_alerts: bool = Field(default=True, description="Send low balance alerts")
    send_api_key_alerts: bool = Field(default=True, description="Send API key security alerts")
    webhook_timeout: int = Field(default=30, description="Webhook timeout in seconds")


class PaymentsSettings(BaseModel):
    """Universal payments module settings."""
    
    # General settings
    enabled: bool = Field(default=True, description="Enable payments module")
    debug_mode: bool = Field(default=False, description="Enable debug mode for payments")
    
    # Component settings
    security: SecuritySettings = Field(default_factory=SecuritySettings)
    rate_limits: RateLimitSettings = Field(default_factory=RateLimitSettings)
    billing: BillingSettings = Field(default_factory=BillingSettings)
    cache: CacheSettings = Field(default_factory=CacheSettings)
    notifications: NotificationSettings = Field(default_factory=NotificationSettings)
    
    # Provider configurations
    providers: Dict[str, PaymentProviderConfig] = Field(default_factory=dict, description="Payment provider configurations")
    
    # Feature flags
    enable_crypto_payments: bool = Field(default=True, description="Enable cryptocurrency payments")
    enable_fiat_payments: bool = Field(default=True, description="Enable fiat currency payments")
    enable_subscription_system: bool = Field(default=True, description="Enable subscription system")
    enable_balance_system: bool = Field(default=True, description="Enable user balance system")
    enable_api_key_system: bool = Field(default=True, description="Enable API key system")
    enable_webhook_processing: bool = Field(default=True, description="Enable webhook processing")
    
    # Backwards compatibility properties
    @property
    def auto_create_api_keys(self) -> bool:
        """Backwards compatibility for auto_create_api_keys."""
        return self.security.auto_create_api_keys
    
    @property
    def min_balance_threshold(self) -> float:
        """Backwards compatibility for min_balance_threshold."""
        return self.security.min_balance_threshold
    
    @property
    def default_rate_limit_per_hour(self) -> int:
        """Backwards compatibility for default_rate_limit_per_hour."""
        return self.rate_limits.default_rate_limit_per_hour
    
    @property
    def default_rate_limit_per_day(self) -> int:
        """Backwards compatibility for default_rate_limit_per_day."""
        return self.rate_limits.default_rate_limit_per_day
    
    @property
    def api_key_length(self) -> int:
        """Backwards compatibility for api_key_length."""
        return self.security.api_key_length
    
    @property
    def api_key_prefix(self) -> str:
        """Backwards compatibility for api_key_prefix."""
        return self.security.api_key_prefix
    
    @property
    def auto_bill_subscriptions(self) -> bool:
        """Backwards compatibility for auto_bill_subscriptions."""
        return self.billing.auto_bill_subscriptions
    
    @property
    def billing_grace_period_hours(self) -> int:
        """Backwards compatibility for billing_grace_period_hours."""
        return self.billing.billing_grace_period_hours
    
    @property
    def cache_timeout_access_check(self) -> int:
        """Backwards compatibility for cache_timeout_access_check."""
        return self.cache.cache_timeout_access_check
    
    @property
    def cache_timeout_user_balance(self) -> int:
        """Backwards compatibility for cache_timeout_user_balance."""
        return self.cache.cache_timeout_user_balance
    
    @property
    def cache_timeout_subscriptions(self) -> int:
        """Backwards compatibility for cache_timeout_subscriptions."""
        return self.cache.cache_timeout_subscriptions

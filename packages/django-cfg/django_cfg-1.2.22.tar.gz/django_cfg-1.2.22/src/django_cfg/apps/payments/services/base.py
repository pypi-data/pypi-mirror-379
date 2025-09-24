"""
Base payment service classes.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from decimal import Decimal


class PaymentProvider(ABC):
    """Abstract base class for payment providers."""
    
    def __init__(self, config: Dict[str, Any]):
        """Initialize provider with config."""
        self.config = config
        self.name = self.__class__.__name__.lower().replace('provider', '')
    
    @abstractmethod
    def create_payment(self, amount: Decimal, currency: str, **kwargs) -> Dict[str, Any]:
        """Create a payment request."""
        pass
    
    @abstractmethod
    def check_payment_status(self, payment_id: str) -> Dict[str, Any]:
        """Check payment status."""
        pass
    
    @abstractmethod
    def process_webhook(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Process webhook payload."""
        pass
    
    @abstractmethod
    def get_supported_currencies(self) -> list[str]:
        """Get list of supported currencies."""
        pass


class PaymentService:
    """Main payment service with provider management."""
    
    def __init__(self):
        """Initialize payment service."""
        self.providers: Dict[str, PaymentProvider] = {}
    
    def register_provider(self, provider: PaymentProvider) -> None:
        """Register a payment provider."""
        self.providers[provider.name] = provider
    
    def get_provider(self, name: str) -> Optional[PaymentProvider]:
        """Get provider by name."""
        return self.providers.get(name)
    
    def create_payment(self, provider_name: str, amount: Decimal, currency: str, **kwargs) -> Dict[str, Any]:
        """Create payment using specified provider."""
        provider = self.get_provider(provider_name)
        if not provider:
            raise ValueError(f"Provider {provider_name} not found")
        
        return provider.create_payment(amount, currency, **kwargs)
    
    def process_webhook(self, provider_name: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Process webhook for specified provider."""
        provider = self.get_provider(provider_name)
        if not provider:
            raise ValueError(f"Provider {provider_name} not found")
        
        return provider.process_webhook(payload)

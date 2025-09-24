"""
Currency managers.
"""

from django.db import models


class CurrencyManager(models.Manager):
    """Manager for Currency model."""
    
    def get_active_currencies(self):
        """Get active currencies."""
        return self.filter(is_active=True)
    
    def get_fiat_currencies(self):
        """Get fiat currencies."""
        return self.filter(currency_type='fiat', is_active=True)
    
    def get_crypto_currencies(self):
        """Get cryptocurrencies."""
        return self.filter(currency_type='crypto', is_active=True)


class CurrencyNetworkManager(models.Manager):
    """Manager for CurrencyNetwork model."""
    
    def get_active_networks(self, currency=None):
        """Get active networks."""
        queryset = self.filter(is_active=True)
        if currency:
            queryset = queryset.filter(currency=currency)
        return queryset

"""
Base model classes for the universal payments system.
"""

from django.db import models


class TimestampedModel(models.Model):
    """Base model with automatic timestamps."""
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
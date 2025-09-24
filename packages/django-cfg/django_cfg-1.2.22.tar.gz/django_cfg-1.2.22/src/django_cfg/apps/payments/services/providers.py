"""
Payment provider integrations using Pydantic for external data validation.
Only for provider responses and internal service communication.
"""

from pydantic import BaseModel, Field, ConfigDict, field_validator
from decimal import Decimal
from datetime import datetime, timezone
from typing import Optional, Dict, Any


class NowPaymentsWebhook(BaseModel):
    """NowPayments webhook data validation."""
    model_config = ConfigDict(validate_assignment=True, extra="forbid")
    
    payment_id: str
    payment_status: str
    pay_address: str
    pay_amount: Decimal
    pay_currency: str
    order_id: str
    order_description: Optional[str] = None
    ipn_callback_url: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    @field_validator('pay_amount')
    @classmethod
    def validate_amount(cls, v: Decimal) -> Decimal:
        if v <= 0:
            raise ValueError("Payment amount must be positive")
        return v


class NowPaymentsCreateResponse(BaseModel):
    """NowPayments payment creation response."""
    model_config = ConfigDict(validate_assignment=True, extra="forbid")
    
    payment_id: str
    payment_status: str
    pay_address: str
    pay_amount: Decimal
    pay_currency: str
    order_id: str
    order_description: Optional[str] = None
    ipn_callback_url: Optional[str] = None
    created_at: datetime
    updated_at: datetime


class NowPaymentsStatusResponse(BaseModel):
    """NowPayments payment status response."""
    model_config = ConfigDict(validate_assignment=True, extra="forbid")
    
    payment_id: str
    payment_status: str
    pay_address: str
    pay_amount: Decimal
    actually_paid: Optional[Decimal] = None
    pay_currency: str
    order_id: str
    outcome_amount: Optional[Decimal] = None
    outcome_currency: Optional[str] = None


class ProviderWebhookData(BaseModel):
    """Generic webhook data for any provider."""
    model_config = ConfigDict(validate_assignment=True, extra="forbid")
    
    provider: str
    payment_id: str
    status: str
    amount: Optional[Decimal] = None
    currency: Optional[str] = None
    raw_data: Dict[str, Any] = Field(default_factory=dict)
    signature: Optional[str] = None
    received_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

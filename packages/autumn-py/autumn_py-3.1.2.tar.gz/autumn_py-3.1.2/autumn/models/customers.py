from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from .entities import Entity

from .customer_meta import (
    CustomerFeature,
    CustomerInvoice,
    CustomerProduct,
    FeatureType,
    ProductStatus,
)
from .env import AppEnv

__all__ = (
    "ProductStatus",
    "FeatureType",
    "CustomerInvoice",
    "CustomerFeature",
    "CustomerProduct",
    "Customer",
    "PriceInfo",
    "ItemInfo",
    "GetPricingTableParams",
    "PricingTableProduct",
)


class Customer(BaseModel):
    id: Optional[str] = None
    created_at: int
    name: Optional[str] = None
    email: Optional[str] = None
    fingerprint: Optional[str] = None
    stripe_id: Optional[str] = None
    env: AppEnv
    metadata: Dict[str, Any]
    products: List[CustomerProduct]
    features: Dict[str, CustomerFeature]
    invoices: Optional[List[CustomerInvoice]] = None
    entities: Optional[List[Entity]] = None


class PriceInfo(BaseModel):
    primaryText: str
    secondaryText: Optional[str] = None


class ItemInfo(BaseModel):
    primaryText: str
    secondaryText: Optional[str] = None


class GetPricingTableParams(BaseModel):
    customer_id: Optional[str] = None


class PricingTableProduct(BaseModel):
    id: str
    name: str
    buttonText: str
    price: PriceInfo
    items: List[ItemInfo]


# Rebuild models to resolve forward references
def _rebuild_models():
    """Rebuild models after all imports are complete to resolve forward references."""
    try:
        from .entities import Entity  # Import here to avoid circular import
        Customer.model_rebuild()
    except ImportError:
        # If entities module isn't available, skip rebuild
        pass


# Call rebuild when module is imported
_rebuild_models()

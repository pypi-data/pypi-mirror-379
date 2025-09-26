from typing import Dict, List, Optional

from pydantic import BaseModel

from .customer_meta import CustomerFeature, CustomerInvoice, CustomerProduct
from .env import AppEnv


class Entity(BaseModel):
    id: str
    name: str
    customer_id: str
    created_at: int
    env: AppEnv
    products: Optional[List[CustomerProduct]] = None
    features: Optional[Dict[str, CustomerFeature]] = None
    invoices: Optional[List[CustomerInvoice]] = None

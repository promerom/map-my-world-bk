from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel


class LocationCategoryReviewed(BaseModel):
    id: Optional[UUID] = uuid4()
    id_location: int
    id_category: int
    reviewed: bool

from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel

from app.v1.schema.category import Category
from app.v1.schema.location import Location


class LocationCategoryReviewed(BaseModel):
    id: Optional[UUID] = uuid4()
    id_location: Location
    id_category: Category
    date_reviewed: datetime
    reviewed: bool


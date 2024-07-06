from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel


class Category(BaseModel):
    id: Optional[UUID] = uuid4()
    type: str



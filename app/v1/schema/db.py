from typing import List
from uuid import uuid4


from app.v1.model.models import Location, Category

categories: List[Category] = [
    Category(
        id=uuid4(),
        type="park"
    ),
    Category(
        id=uuid4(),
        type="house"
    ),
    Category(
        id=uuid4(),
        type="stadium"
    )
]

locations: List[Location] = [
    Location(
        id=uuid4(),
        name="Location 1",
        longitude="1.2.3.4.5.6",
        latitude="6.5.4.3.2.1",
        category=next((cat for cat in categories if cat.type == "stadium"), None)
    ),
    Location(
        id=uuid4(),
        name="Location 2",
        longitude="2.3.4.5.6.7",
        latitude="7.6.5.4.3.2",
        category=next((cat for cat in categories if cat.type == "house"), None)
    )
]

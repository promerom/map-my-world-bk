from typing import List
from uuid import uuid4


from app.v1.schema.category import Category
from app.v1.schema.location import Location

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
        latitude="6.5.4.3.2.1"
    ),
    Location(
        id=uuid4(),
        name="Location 2",
        longitude="2.3.4.5.6.7",
        latitude="7.6.5.4.3.2"
    )
]

from datetime import datetime
from uuid import uuid4

from fastapi import FastAPI

from app.v1.schema.category import Category
from app.v1.schema.location import Location
from app.v1.model import db, location_category_reviewed
from app.v1.schema.location_category_reviewed import LocationCategoryReviewed

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello World!"}


@app.get("/api/v1/locations")
def locations():
    return db.locations


@app.get("/api/v1/categories")
async def categories():
    return db.categories


@app.post("/api/v1/add/location")
async def create_location(location: Location):
    db.locations.append(location)
    return {"id": location.id}


@app.post("/api/v1/add/category")
async def create_category(category: Category):
    db.categories.append(category)
    return {"id": category.id}


@app.get("/api/v1/review")
async def review():
    return location_category_reviewed.locations_and_categories_reviewed


@app.post("/api/v1/reviewed")
async def reviewed(category: Category, location: Location):
    loc_cat_reviewed = LocationCategoryReviewed(
        id=uuid4(),
        id_location=next((loc for loc in db.locations if loc.name == location.name), None),
        id_category=next((cat for cat in db.categories if cat.type == category.type), None),
        date_reviewed=datetime.now(),
        reviewed=True
    )

    location_category_reviewed.locations_and_categories_reviewed.append(loc_cat_reviewed)
    return {"location and category reviewed"}

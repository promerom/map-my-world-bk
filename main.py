from datetime import datetime, timedelta
from uuid import uuid4, UUID

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
    today = datetime.now()
    yesterday = datetime.now() - timedelta(days=2)
    days = today - yesterday

    for_review = []
    for lcr in location_category_reviewed.locations_and_categories_reviewed:
        days_since_review = datetime.now() - lcr.date_reviewed
        if lcr.reviewed == False or days_since_review.days > 29:
            for_review.append(lcr)
            if len(for_review) > 9:
                break

    return for_review


@app.get("/api/v1/locations-and-categories")
async def locations_and_categories():
    for cat in db.categories:
        for loc in db.locations:
            location_category_reviewed.locations_and_categories_reviewed.append(
                LocationCategoryReviewed(
                    id=uuid4(),
                    id_category=cat,
                    id_location=loc,
                    date_reviewed=datetime.now()
                )
            )
    return location_category_reviewed.locations_and_categories_reviewed


@app.post("/api/v1/reviewed")
async def reviewed(id_location_category_reviewed: UUID):
    for location_category_for_review in location_category_reviewed.locations_and_categories_reviewed:
        if location_category_for_review.id == id_location_category_reviewed:
            location_category_for_review.reviewed = True
            location_category_for_review.date_reviewed = datetime.now()
            break

    return {f"location and category reviewed %s\n" % id_location_category_reviewed}

from fastapi import FastAPI

from app.v1.schema.category import Category
from app.v1.schema.location import Location
from app.v1.model import db

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello World!"}


@app.get("/api/v1/locations")
def location():
    return db.locations


@app.get("/api/v1/categories")
def categories():
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
    return {"review this locations"}

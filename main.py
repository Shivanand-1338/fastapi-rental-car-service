from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI()

# Dummy DB
cars = [
    {
        "id": 1,
        "brand": "Toyota",
        "model": "Innova",
        "price_per_day": 2500,
        "available": True
    },
    {
        "id": 2,
        "brand": "Hyundai",
        "model": "Creta",
        "price_per_day": 2000,
        "available": True
    },
    {
        "id": 3,
        "brand": "Maruti",
        "model": "Swift",
        "price_per_day": 1200,
        "available": True
    },
    {
        "id": 4,
        "brand": "Mahindra",
        "model": "Thar",
        "price_per_day": 3000,
        "available": True
    },
    {
        "id": 5,
        "brand": "Honda",
        "model": "City",
        "price_per_day": 1800,
        "available": True
    },
    {
        "id": 6,
        "brand": "Tata",
        "model": "Nexon",
        "price_per_day": 1700,
        "available": True
    },
    {
        "id": 7,
        "brand": "Kia",
        "model": "Seltos",
        "price_per_day": 2200,
        "available": True
    }
]
rentals = []

# Models
class Car(BaseModel):
    id: int
    brand: str
    model: str = Field(..., min_length=2)
    price_per_day: float = Field(..., gt=0)
    available: bool = True

class RentRequest(BaseModel):
    car_id: int
    user_name: str
    days: int = Field(..., gt=0)

# Helper Functions
def find_car(car_id: int):
    for car in cars:
        if car["id"] == car_id:
            return car
    return None

def calculate_total(price, days):
    return price * days

# Home
@app.get("/")
def home():
    return {"message": "Car Rental API Running "}

# Get all cars
@app.get("/cars")
def get_cars(
    keyword: Optional[str] = None,
    sort_by: Optional[str] = None,
    page: int = 1,
    limit: int = 5
):
    result = cars

    # Search
    if keyword:
        result = [c for c in result if keyword.lower() in c["model"].lower()]

    # Sorting
    if sort_by == "price":
        result = sorted(result, key=lambda x: x["price_per_day"])

    # Pagination
    start = (page - 1) * limit
    end = start + limit

    return result[start:end]

# Count
@app.get("/cars/count")
def count_cars():
    return {"total": len(cars)}

# Get by ID
@app.get("/cars/{car_id}")
def get_car(car_id: int):
    car = find_car(car_id)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

# Create Car
@app.post("/cars", status_code=201)
def create_car(car: Car):
    cars.append(car.dict())
    return car




class CarUpdate(BaseModel):
    brand: Optional[str] = None
    model: Optional[str] = None
    price_per_day: Optional[float] = Field(None, gt=0)
    available: Optional[bool] = None




@app.put("/cars/{car_id}")
def update_car(car_id: int, updated: CarUpdate):
    car = find_car(car_id)

    if not car:
        raise HTTPException(status_code=404, detail="Car not found")

    update_data = updated.dict(exclude_unset=True)

    for key, value in update_data.items():
        car[key] = value

    return {"message": "Car updated successfully", "car": car}

# Delete Car
@app.delete("/cars/{car_id}")
def delete_car(car_id: int):
    car = find_car(car_id)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")

    cars.remove(car)
    return {"message": "Car deleted"}

# -------------------------------
# 🚀 MULTI-STEP WORKFLOW
# -------------------------------

# Rent Car
@app.post("/rent")
def rent_car(request: RentRequest):
    car = find_car(request.car_id)

    if not car:
        raise HTTPException(status_code=404, detail="Car not found")

    if not car["available"]:
        raise HTTPException(status_code=400, detail="Car not available")

    total_cost = calculate_total(car["price_per_day"], request.days)

    rental = {
        "car_id": request.car_id,
        "user": request.user_name,
        "days": request.days,
        "total_cost": total_cost
    }

    rentals.append(rental)
    car["available"] = False

    return {"message": "Car rented successfully", "details": rental}

# Return Car
@app.post("/return/{car_id}")
def return_car(car_id: int):
    car = find_car(car_id)

    if not car:
        raise HTTPException(status_code=404, detail="Car not found")

    car["available"] = True
    return {"message": "Car returned successfully"}

# Rental History
@app.get("/rentals")
def rental_history():
    return rentals
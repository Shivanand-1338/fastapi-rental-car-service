# 🚗 Car Rental API (FastAPI)

A simple and scalable **Car Rental REST API** built using **FastAPI**.
This project demonstrates CRUD operations, filtering, pagination, and a multi-step rental workflow.

---

## 📌 Features

* 🚘 Manage cars (CRUD operations)
* 🔍 Search cars by keyword
* 📊 Sort cars by price
* 📄 Pagination support
* 📦 Count total cars
* 🔁 Rent & return cars (multi-step workflow)
* 📜 Rental history tracking
* ✅ Input validation using Pydantic

---

## 🏗️ Project Structure

```
car-rental-api/
│
├── main.py              # Main FastAPI application
├── README.md           # Project documentation
└── requirements.txt    # Dependencies
```

---

## ⚙️ Tech Stack

* Python 3.8+
* FastAPI
* Pydantic
* Uvicorn (ASGI server)

---

## 🚀 Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/car-rental-api.git
cd car-rental-api
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:



### 4. Install dependencies

```bash
pip install fastapi uvicorn
```

---

## ▶️ Run the Application

```bash
uvicorn main:app --reload
```

App will be available at:

* API: http://127.0.0.1:8000
* Docs (Swagger): http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

---

## 📡 API Endpoints

### 🏠 Home

```
GET /
```

Returns API status message.

---

### 🚘 Car APIs

#### Get all cars

```
GET /cars
```

Query Params:

* `keyword` → search by model
* `sort_by=price` → sort by price
* `page` → pagination page (default: 1)
* `limit` → items per page (default: 5)

---

#### Get car count

```
GET /cars/count
```

---

#### Get car by ID

```
GET /cars/{car_id}
```

---

#### Create a car

```
POST /cars
```

Request Body:

```json
{
  "id": 8,
  "brand": "Ford",
  "model": "EcoSport",
  "price_per_day": 1600,
  "available": true
}
```

---

#### Update a car

```
PUT /cars/{car_id}
```

---

#### Delete a car

```
DELETE /cars/{car_id}
```

---

## 🔁 Rental Workflow

### Rent a car

```
POST /rent
```

Request Body:

```json
{
  "car_id": 1,
  "user_name": "John",
  "days": 3
}
```

✔️ Validates:

* Car exists
* Car is available

✔️ Actions:

* Calculates total cost
* Marks car as unavailable
* Stores rental record

---

### Return a car

```
POST /return/{car_id}
```

✔️ Marks the car as available again

---

### Rental history

```
GET /rentals
```

Returns all rental records.

---

## 🧠 Core Concepts Explained

### 1. In-Memory Database

* Uses Python lists (`cars`, `rentals`)
* No external DB required
* Good for learning and prototyping

---

### 2. Pydantic Models

```python
class Car(BaseModel):
    id: int
    brand: str
    model: str
    price_per_day: float
    available: bool
```

✔️ Ensures:

* Data validation
* Type safety
* Clean request handling

---

### 3. Filtering & Pagination

```python
start = (page - 1) * limit
end = start + limit
```

* Efficient slicing of results
* Improves performance

---

### 4. Business Logic

* `find_car()` → locate car
* `calculate_total()` → pricing logic

---

### 5. Multi-Step Workflow

#### Rent Flow:

1. Validate car
2. Check availability
3. Calculate cost
4. Store rental
5. Update car status

---

## 🧪 Example Workflow

1. Get available cars
2. Rent a car
3. Try renting again (fails)
4. Return the car
5. Rent again (success)



## 🔮 Future Improvements

* 🔐 Authentication (JWT)
* 🗄️ Database integration (PostgreSQL / MongoDB)
* 💳 Payment gateway
* 📅 Booking dates instead of days
* 🧾 Invoice generation
* 🚀 Docker support

---

## 👨‍💻 Author

Developed for learning FastAPI and backend workflows.

---



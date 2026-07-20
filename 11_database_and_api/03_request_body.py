# ============================================================
# 📘 Lesson 3: Request Body & Pydantic Models
# ============================================================
# So far we've only READ data (GET requests with path params).
# Now we'll learn to SEND data to the API using Request Body.
#
# Request Body = JSON data sent with POST/PUT requests.
# Pydantic = Library that validates the data automatically.
#
# Think of it like filling out a form:
#   - Pydantic defines WHAT the form fields are
#   - FastAPI checks the form is filled correctly
#   - Your code runs only if everything is valid
#
# To run this lesson:
#   python3 -m uvicorn 03_request_body:app --reload
#
# Then open in browser:
#   http://127.0.0.1:8000/docs   ← Test all endpoints here!
# ============================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

# ============================================================
# 📗 Create the FastAPI App
# ============================================================

app = FastAPI(
    title="📘 Request Body & Pydantic Lesson",
    description="Learning to send data to APIs using Pydantic models",
    version="1.0.0",
)

# ============================================================
# 📗 PART 1: Your First Pydantic Model
# ============================================================
# A Pydantic model is a CLASS that defines the structure of
# your data. Inherit from BaseModel.
#
# Required fields  → just type hint:  name: str
# Optional fields  → add a default:   grade: str = "N/A"
# Nullable fields  → use Optional:    city: Optional[str] = None

# --- Define the model ---
class StudentCreate(BaseModel):
    """
    This model defines what data is needed to create a student.
    Think of it as a FORM with these fields.
    """
    name: str                           # Required — must be a string
    age: int                            # Required — must be an integer
    grade: str = "N/A"                  # Optional — defaults to "N/A"
    city: Optional[str] = None          # Optional — can be None/null

# --- Our "database" (a list for now) ---
students_db: list = []
next_id = 1


# --- The endpoint ---
# Try in /docs → POST /students → Try it out
# Send: {"name": "Amitesh", "age": 25, "city": "Pune"}

@app.post("/students", status_code=201)
def create_student(student: StudentCreate):
    """
    Create a new student.

    FastAPI sees `student: StudentCreate` and knows:
    1. Read the JSON body from the request
    2. Validate it against the StudentCreate model
    3. If valid → call this function with the data
    4. If invalid → auto-return 422 error (your code never runs!)
    """
    global next_id

    new_student = {
        "id": next_id,
        "name": student.name,       # Access fields with dot notation!
        "age": student.age,
        "grade": student.grade,     # Will be "N/A" if not provided
        "city": student.city,       # Will be None if not provided
        "created_at": datetime.now().isoformat(),
    }
    students_db.append(new_student)
    next_id += 1

    return {"message": f"Student '{student.name}' created!", "student": new_student}


# --- List all students (to verify our POSTs worked) ---
@app.get("/students")
def list_students():
    """List all students in the database."""
    return {"total": len(students_db), "students": students_db}


# ============================================================
# 📗 PART 2: Pydantic Auto-Validation Demo
# ============================================================
# Try sending INVALID data in /docs to see the automatic
# error responses!
#
# ✅ Valid:   {"name": "Amitesh", "age": 25}
# ✅ Valid:   {"name": "Priya", "age": "23"}    ← auto-converts!
# ❌ Invalid: {"name": "X"}                      ← age missing!
# ❌ Invalid: {"name": 123, "age": 25}           ← name not string!
# ❌ Invalid: {"name": "A", "age": "abc"}        ← age not number!
# ❌ Invalid: "not json at all"                   ← not valid JSON!
#
# FastAPI returns a detailed 422 error with EXACTLY what's wrong!


# ============================================================
# 📗 PART 3: Field Validation with Field()
# ============================================================
# Want stricter rules? Use Field() to add constraints.
# This gives you AUTOMATIC validation — no manual if/else!

class ProductCreate(BaseModel):
    """Product model with strict validation rules."""
    name: str = Field(
        min_length=2,               # At least 2 characters
        max_length=100,             # At most 100 characters
        description="Product name"
    )
    price: float = Field(
        gt=0,                       # Greater than 0 (no free or negative!)
        description="Price in INR"
    )
    stock: int = Field(
        ge=0,                       # Greater or equal to 0
        description="Items in stock"
    )
    category: str = Field(
        default="General",
        description="Product category"
    )
    on_sale: bool = Field(
        default=False,
        description="Is the product on sale?"
    )

    # This is shown as example in the Swagger docs:
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Laptop",
                "price": 85000.0,
                "stock": 15,
                "category": "Electronics",
                "on_sale": True,
            }
        }


# --- Our product "database" ---
products_db: list = []
product_next_id = 1

# Try in /docs:
# ✅ {"name": "Laptop", "price": 85000, "stock": 15}
# ❌ {"name": "X", "price": 85000, "stock": 15}    ← name too short!
# ❌ {"name": "Laptop", "price": -100, "stock": 15} ← negative price!
# ❌ {"name": "Laptop", "price": 85000, "stock": -5} ← negative stock!

@app.post("/products", status_code=201)
def create_product(product: ProductCreate):
    """
    Create a new product with validation.

    Field() constraints are checked AUTOMATICALLY:
    - name: 2-100 characters
    - price: must be > 0
    - stock: must be >= 0
    """
    global product_next_id

    new_product = {
        "id": product_next_id,
        "name": product.name,
        "price": product.price,
        "stock": product.stock,
        "category": product.category,
        "on_sale": product.on_sale,
    }
    products_db.append(new_product)
    product_next_id += 1

    return {"message": f"Product '{product.name}' created!", "product": new_product}


@app.get("/products")
def list_products():
    """List all products."""
    return {"total": len(products_db), "products": products_db}


# ============================================================
# 📗 PART 4: Nested Models (Model inside Model)
# ============================================================
# Real-world data is often nested — Pydantic handles it!
# Just use one model inside another.

class Address(BaseModel):
    """Address sub-model — used inside other models."""
    street: str
    city: str
    state: str = "Maharashtra"
    pin_code: str

class ContactCreate(BaseModel):
    """Contact with a nested Address model."""
    name: str = Field(min_length=2)
    phone: str = Field(min_length=10, max_length=15)
    email: str
    address: Address                # ← Nested model!

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Amitesh",
                "phone": "+91-9876543210",
                "email": "amitesh@example.com",
                "address": {
                    "street": "123 Main Road",
                    "city": "Pune",
                    "state": "Maharashtra",
                    "pin_code": "411001"
                }
            }
        }

contacts_db: list = []
contact_next_id = 1

# Try sending nested JSON in /docs!
@app.post("/contacts", status_code=201)
def create_contact(contact: ContactCreate):
    """
    Create a contact with nested address.

    The 'address' field must be a JSON object matching
    the Address model structure.
    """
    global contact_next_id

    new_contact = {
        "id": contact_next_id,
        "name": contact.name,
        "phone": contact.phone,
        "email": contact.email,
        "address": {
            "street": contact.address.street,     # Nested access!
            "city": contact.address.city,
            "state": contact.address.state,
            "pin_code": contact.address.pin_code,
        }
    }
    contacts_db.append(new_contact)
    contact_next_id += 1

    return {"message": f"Contact '{contact.name}' created!", "contact": new_contact}


@app.get("/contacts")
def list_contacts():
    """List all contacts."""
    return {"total": len(contacts_db), "contacts": contacts_db}


# ============================================================
# 📗 PART 5: List Fields (Arrays in JSON)
# ============================================================
# Use List[type] for fields that accept multiple values.

class OrderCreate(BaseModel):
    """Order with a list of items."""
    customer_name: str = Field(min_length=2)
    items: List[str] = Field(
        min_length=1,                 # At least 1 item required!
        description="List of item names"
    )
    total: float = Field(gt=0)
    notes: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "customer_name": "Amitesh",
                "items": ["Laptop", "Mouse", "Keyboard"],
                "total": 87000.0,
                "notes": "Deliver before Friday"
            }
        }

orders_db: list = []
order_next_id = 1

@app.post("/orders", status_code=201)
def create_order(order: OrderCreate):
    """
    Create a new order.

    The 'items' field must be a list of strings.
    At least 1 item is required.
    """
    global order_next_id

    new_order = {
        "id": order_next_id,
        "customer_name": order.customer_name,
        "items": order.items,
        "item_count": len(order.items),
        "total": order.total,
        "notes": order.notes,
        "status": "pending",
    }
    orders_db.append(new_order)
    order_next_id += 1

    return {"message": f"Order created for '{order.customer_name}'!", "order": new_order}


@app.get("/orders")
def list_orders():
    """List all orders."""
    return {"total": len(orders_db), "orders": orders_db}


# ============================================================
# 📗 PART 6: Separate Models for Create vs Update
# ============================================================
# In real APIs you often have DIFFERENT models for:
#   - Creating (all fields required)
#   - Updating (all fields optional — only send what changed)
#
# This is a common pattern called "schemas".

class TaskCreate(BaseModel):
    """Model for CREATING a task — title is required."""
    title: str = Field(min_length=2, max_length=200)
    description: Optional[str] = None
    priority: str = Field(default="medium")     # low, medium, high

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Learn FastAPI",
                "description": "Complete the Pydantic lesson",
                "priority": "high"
            }
        }


class TaskUpdate(BaseModel):
    """
    Model for UPDATING a task — ALL fields are optional.
    Only send the fields you want to change!
    """
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    completed: Optional[bool] = None

    class Config:
        json_schema_extra = {
            "example": {
                "priority": "low",
                "completed": True
            }
        }


tasks_db: list = []
task_next_id = 1


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    """Create a new task."""
    global task_next_id

    new_task = {
        "id": task_next_id,
        "title": task.title,
        "description": task.description,
        "priority": task.priority,
        "completed": False,
    }
    tasks_db.append(new_task)
    task_next_id += 1

    return {"message": f"Task created!", "task": new_task}


@app.get("/tasks")
def list_tasks():
    """List all tasks."""
    return {"total": len(tasks_db), "tasks": tasks_db}


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    """Get a specific task by ID."""
    for task in tasks_db:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}")
def update_task(task_id: int, updates: TaskUpdate):
    """
    Update a task — send only the fields you want to change.

    This uses TaskUpdate where ALL fields are Optional.
    We use model.dict(exclude_unset=True) to get only the
    fields that were actually sent.
    """
    for task in tasks_db:
        if task["id"] == task_id:
            # Get only fields that were sent (not None)
            update_data = updates.dict(exclude_unset=True)
            for key, value in update_data.items():
                if value is not None:
                    task[key] = value
            return {"message": "Task updated!", "task": task}

    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    """Delete a task by ID."""
    for i, task in enumerate(tasks_db):
        if task["id"] == task_id:
            deleted = tasks_db.pop(i)
            return {"message": f"Task '{deleted['title']}' deleted!"}
    raise HTTPException(status_code=404, detail="Task not found")


# ============================================================
# 📗 PART 7: Path Params + Body + Query Params Together
# ============================================================
# You can combine ALL three in one endpoint!
#   - Path params   → identifies the resource
#   - Request body  → the data to send
#   - Query params  → options/flags

class ReviewCreate(BaseModel):
    """Review model for a product."""
    rating: int = Field(ge=1, le=5, description="Rating from 1 to 5")
    comment: str = Field(min_length=5, max_length=500)
    reviewer: str = Field(min_length=2)

    class Config:
        json_schema_extra = {
            "example": {
                "rating": 5,
                "comment": "Amazing product, highly recommended!",
                "reviewer": "Amitesh"
            }
        }

reviews_db: list = []

@app.post("/products/{product_id}/reviews")
def add_review(
    product_id: int,             # ← PATH parameter (from URL)
    review: ReviewCreate,        # ← REQUEST BODY (from JSON)
    notify: bool = False,        # ← QUERY parameter (from ?notify=true)
):
    """
    Add a review to a product.

    Combines all three:
    - product_id: path parameter → which product
    - review: request body → the review data
    - notify: query parameter → send notification?

    Try: POST /products/1/reviews?notify=true
    With body: {"rating": 5, "comment": "Great product!", "reviewer": "Amitesh"}
    """
    new_review = {
        "product_id": product_id,
        "rating": review.rating,
        "comment": review.comment,
        "reviewer": review.reviewer,
        "notification_sent": notify,
    }
    reviews_db.append(new_review)

    return {
        "message": "Review added!",
        "review": new_review,
        "notification": "📧 Notification sent!" if notify else "No notification",
    }


@app.get("/products/{product_id}/reviews")
def get_reviews(product_id: int):
    """Get all reviews for a product."""
    product_reviews = [r for r in reviews_db if r["product_id"] == product_id]
    return {
        "product_id": product_id,
        "total_reviews": len(product_reviews),
        "reviews": product_reviews,
    }


# ============================================================
# 📗 PART 8: Model Methods — .dict() and .json()
# ============================================================
# Pydantic models have useful built-in methods.

@app.post("/demo/model-methods")
def model_methods_demo(student: StudentCreate):
    """
    Demonstrates Pydantic model's built-in methods.

    - .dict()  → Convert model to dictionary
    - .json()  → Convert model to JSON string
    - .copy()  → Create a copy (with optional updates)
    """
    return {
        "as_dict": student.dict(),                    # → Python dict
        "as_json": student.json(),                    # → JSON string
        "fields": list(student.__fields__.keys()),    # → Field names
        "field_count": len(student.__fields__),
    }


# ============================================================
# 📗 Root Endpoint — Summary of All Routes
# ============================================================

@app.get("/")
def root():
    """Welcome page — lists all available endpoints."""
    return {
        "message": "📘 Request Body & Pydantic Models Lesson",
        "tip": "Visit /docs for interactive Swagger UI!",
        "endpoints": {
            "students": {
                "POST /students": "Create a student (basic model)",
                "GET /students": "List all students",
            },
            "products": {
                "POST /products": "Create a product (Field validation)",
                "GET /products": "List all products",
            },
            "contacts": {
                "POST /contacts": "Create a contact (nested model)",
                "GET /contacts": "List all contacts",
            },
            "orders": {
                "POST /orders": "Create an order (list fields)",
                "GET /orders": "List all orders",
            },
            "tasks (full CRUD)": {
                "POST /tasks": "Create a task",
                "GET /tasks": "List all tasks",
                "GET /tasks/{id}": "Get one task",
                "PUT /tasks/{id}": "Update a task (partial update)",
                "DELETE /tasks/{id}": "Delete a task",
            },
            "reviews": {
                "POST /products/{id}/reviews": "Add review (path + body + query)",
                "GET /products/{id}/reviews": "Get reviews for a product",
            },
        },
    }


# ============================================================
# 📗 HOW TO RUN THIS LESSON
# ============================================================
#
# 1. Open terminal:
#      cd 11_database_and_api
#
# 2. Start the server:
#      python3 -m uvicorn 03_request_body:app --reload
#
# 3. Open browser:
#      http://127.0.0.1:8000/docs     ← Swagger UI
#
# 4. In Swagger UI:
#      - Click on a POST endpoint
#      - Click "Try it out"
#      - Edit the JSON body
#      - Click "Execute"
#      - See the response!
#
# 5. Try sending INVALID data to see the 422 errors!
#
# 6. Press Ctrl+C to stop the server.
#
# ============================================================
# 🏋️ PRACTICE:
# ============================================================
# 1. Create a BookCreate model with:
#    title (str, min 2 chars), author (str), year (int, 1000-2026),
#    rating (float, 1-5), genre (optional str)
#    Build POST /books and GET /books endpoints.
#
# 2. Create a nested model: CompanyCreate with
#    name, industry, and a nested "ceo" field that has
#    name, age, and email.
#
# 3. Build a full CRUD for a "notes" app:
#    POST /notes, GET /notes, GET /notes/{id},
#    PUT /notes/{id}, DELETE /notes/{id}
#    Use separate NoteCreate and NoteUpdate models.
#
# 4. Create a POST /calculate endpoint that takes a body:
#    {"numbers": [1,2,3,4,5], "operation": "sum"}
#    Support: sum, average, min, max, product
#
# 5. Build POST /register with username, email, password.
#    Validate: username 3-20 chars, password min 8 chars.
# ============================================================

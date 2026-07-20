# ============================================================
# 📘 Lesson 2: FastAPI Path Parameters
# ============================================================
# Path Parameters are VARIABLE parts of a URL.
# Instead of writing separate functions for /users/1, /users/2,
# /users/3 — you write ONE function that handles ALL of them.
#
# Example:
#   @app.get("/users/{user_id}")
#   def get_user(user_id: int):
#       return {"id": user_id}
#
# The {user_id} part is the PATH PARAMETER.
# FastAPI automatically:
#   1. EXTRACTS the value from the URL
#   2. CONVERTS it to your type hint (int, str, etc.)
#   3. VALIDATES it (rejects wrong types with 422 error)
#
# To run this lesson:
#   python3 -m uvicorn 02_path_parameters:app --reload
#
# Then open in browser:
#   http://127.0.0.1:8000/docs   ← Interactive Swagger UI
# ============================================================

from fastapi import FastAPI, HTTPException

# ============================================================
# 📗 Create the FastAPI App
# ============================================================
# FastAPI() creates your application — like starting a new
# web server. Every route/endpoint is attached to this app.

app = FastAPI(
    title="📘 Path Parameters Lesson",
    description="Learning path parameters in FastAPI step by step",
    version="1.0.0",
)

# ============================================================
# 📗 PART 1: Basic Path Parameter
# ============================================================
# The simplest path parameter — just put {name} in the URL
# and accept it as a function argument with the SAME name.
#
# Try these URLs in your browser:
#   http://127.0.0.1:8000/hello/Amitesh
#   http://127.0.0.1:8000/hello/Priya
#   http://127.0.0.1:8000/hello/World

@app.get("/hello/{name}")
def say_hello(name: str):
    """
    Greet a person by name.

    The {name} in the URL becomes the `name` argument.
    - /hello/Amitesh → name = "Amitesh"
    - /hello/Priya   → name = "Priya"
    """
    return {
        "message": f"Hello, {name}! 👋",
        "parameter_received": name,
        "parameter_type": type(name).__name__,
    }


# ============================================================
# 📗 PART 2: Path Parameter with Type Conversion
# ============================================================
# Add a TYPE HINT and FastAPI auto-converts the value.
# If the type doesn't match, it returns a 422 error!
#
# Try:
#   http://127.0.0.1:8000/square/5      ✅ → 25
#   http://127.0.0.1:8000/square/10     ✅ → 100
#   http://127.0.0.1:8000/square/abc    ❌ → 422 error!

@app.get("/square/{number}")
def calculate_square(number: int):
    """
    Calculate the square of a number.

    Type hint `int` means FastAPI will:
    1. Extract "5" from the URL
    2. Convert it to int → 5
    3. Reject non-integers with 422 error
    """
    return {
        "number": number,
        "square": number ** 2,
        "type": type(number).__name__,   # Will be "int" not "str"!
    }


# ============================================================
# 📗 PART 3: Float Path Parameter
# ============================================================
# Works with float too — FastAPI converts automatically.
#
# Try:
#   http://127.0.0.1:8000/temperature/36.6
#   http://127.0.0.1:8000/temperature/100.0
#   http://127.0.0.1:8000/temperature/0

@app.get("/temperature/{celsius}")
def convert_temperature(celsius: float):
    """
    Convert Celsius to Fahrenheit.

    Type hint `float` accepts both integers and decimals.
    """
    fahrenheit = (celsius * 9 / 5) + 32
    return {
        "celsius": celsius,
        "fahrenheit": round(fahrenheit, 2),
        "status": "🥶 Cold" if celsius < 15 else "😊 Normal" if celsius < 35 else "🔥 Hot",
    }


# ============================================================
# 📗 PART 4: Simulating a Database with a Dictionary
# ============================================================
# In real apps, you'd fetch from a database.
# For learning, we'll use a dictionary as our "database".

STUDENTS_DB = {
    1: {"id": 1, "name": "Amitesh", "age": 25, "grade": "A",  "city": "Pune"},
    2: {"id": 2, "name": "Priya",   "age": 23, "grade": "A+", "city": "Mumbai"},
    3: {"id": 3, "name": "Rahul",   "age": 24, "grade": "B+", "city": "Delhi"},
    4: {"id": 4, "name": "Sneha",   "age": 22, "grade": "A",  "city": "Bangalore"},
    5: {"id": 5, "name": "Arjun",   "age": 26, "grade": "B",  "city": "Chennai"},
}

COURSES_DB = {
    "python":     {"code": "CS101", "name": "Python Programming", "credits": 4, "instructor": "Dr. Sharma"},
    "javascript": {"code": "CS102", "name": "JavaScript Basics",  "credits": 3, "instructor": "Prof. Gupta"},
    "database":   {"code": "CS201", "name": "Database Systems",   "credits": 4, "instructor": "Dr. Patel"},
    "web":        {"code": "CS202", "name": "Web Development",    "credits": 3, "instructor": "Prof. Singh"},
}


# ============================================================
# 📗 PART 5: Path Parameter to Fetch a Resource
# ============================================================
# The most common use: get a SPECIFIC item by its ID.
#
# Try:
#   http://127.0.0.1:8000/students/1     ✅ → Amitesh's data
#   http://127.0.0.1:8000/students/3     ✅ → Rahul's data
#   http://127.0.0.1:8000/students/99    ❌ → 404 Not Found

@app.get("/students/{student_id}")
def get_student(student_id: int):
    """
    Get a student by their ID.

    - If found → returns student data (200 OK)
    - If not found → raises 404 error
    """
    if student_id not in STUDENTS_DB:
        # HTTPException sends a proper error response
        raise HTTPException(
            status_code=404,
            detail=f"Student with ID {student_id} not found"
        )
    return STUDENTS_DB[student_id]


# ============================================================
# 📗 PART 6: String Path Parameter (Lookup by Name)
# ============================================================
# Path parameters can be strings too — not just numbers!
#
# Try:
#   http://127.0.0.1:8000/courses/python
#   http://127.0.0.1:8000/courses/database
#   http://127.0.0.1:8000/courses/rust      ❌ → 404

@app.get("/courses/{course_name}")
def get_course(course_name: str):
    """
    Get course details by name (case-insensitive).

    String path parameters keep the exact value from the URL.
    We use .lower() to make the search case-insensitive.
    """
    key = course_name.lower()
    if key not in COURSES_DB:
        raise HTTPException(
            status_code=404,
            detail=f"Course '{course_name}' not found. Available: {list(COURSES_DB.keys())}"
        )
    return COURSES_DB[key]


# ============================================================
# 📗 PART 7: Multiple Path Parameters
# ============================================================
# You can have MULTIPLE path parameters in one URL.
# Each {param} maps to a function argument.
#
# Try:
#   http://127.0.0.1:8000/math/add/10/5       → 15
#   http://127.0.0.1:8000/math/subtract/10/5  → 5
#   http://127.0.0.1:8000/math/multiply/10/5  → 50
#   http://127.0.0.1:8000/math/divide/10/5    → 2.0
#   http://127.0.0.1:8000/math/divide/10/0    ❌ → 400 error

@app.get("/math/{operation}/{a}/{b}")
def calculator(operation: str, a: float, b: float):
    """
    Perform math with path parameters.

    Three path parameters:
    - {operation}: add, subtract, multiply, divide
    - {a}: first number
    - {b}: second number
    """
    operations = {
        "add":      lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide":   lambda x, y: x / y if y != 0 else None,
    }

    if operation not in operations:
        raise HTTPException(
            status_code=400,
            detail=f"Unknown operation '{operation}'. Use: {list(operations.keys())}"
        )

    if operation == "divide" and b == 0:
        raise HTTPException(
            status_code=400,
            detail="Cannot divide by zero!"
        )

    result = operations[operation](a, b)
    return {
        "operation": operation,
        "a": a,
        "b": b,
        "result": result,
        "expression": f"{a} {operation} {b} = {result}",
    }


# ============================================================
# 📗 PART 8: Nested Path Parameters (Resource Hierarchy)
# ============================================================
# Real APIs often have nested resources:
#   /students/1/grades → grades for student #1
#
# Try:
#   http://127.0.0.1:8000/students/1/profile
#   http://127.0.0.1:8000/students/2/profile

GRADES_DB = {
    1: {"math": 90, "science": 85, "english": 92, "python": 95},
    2: {"math": 95, "science": 90, "english": 88, "python": 98},
    3: {"math": 78, "science": 72, "english": 80, "python": 85},
    4: {"math": 88, "science": 92, "english": 86, "python": 90},
    5: {"math": 70, "science": 68, "english": 75, "python": 72},
}

@app.get("/students/{student_id}/profile")
def get_student_profile(student_id: int):
    """
    Get full profile of a student (info + grades + stats).

    Nested resource: /students/{id}/profile
    Uses two data sources: STUDENTS_DB and GRADES_DB
    """
    if student_id not in STUDENTS_DB:
        raise HTTPException(status_code=404, detail="Student not found")

    student = STUDENTS_DB[student_id]
    grades = GRADES_DB.get(student_id, {})

    # Calculate stats
    if grades:
        avg = sum(grades.values()) / len(grades)
        highest_subject = max(grades, key=lambda x: grades[x])
        lowest_subject = min(grades, key=lambda x: grades[x])
    else:
        avg = 0
        highest_subject = lowest_subject = "N/A"

    return {
        "student": student,
        "grades": grades,
        "stats": {
            "average": round(avg, 2),
            "highest": {"subject": highest_subject, "score": grades.get(highest_subject, 0)},
            "lowest": {"subject": lowest_subject, "score": grades.get(lowest_subject, 0)},
            "total_subjects": len(grades),
        }
    }


# ============================================================
# 📗 PART 9: Path Parameter for a Specific Sub-Resource
# ============================================================
# Go even deeper: /students/1/grades/math
#
# Try:
#   http://127.0.0.1:8000/students/1/grades/math
#   http://127.0.0.1:8000/students/2/grades/python
#   http://127.0.0.1:8000/students/1/grades/history  ❌ → 404

@app.get("/students/{student_id}/grades/{subject}")
def get_student_grade(student_id: int, subject: str):
    """
    Get a specific grade for a specific student.

    Two path parameters:
    - {student_id}: which student
    - {subject}: which subject

    /students/1/grades/math → Amitesh's math grade
    """
    if student_id not in STUDENTS_DB:
        raise HTTPException(status_code=404, detail="Student not found")

    grades = GRADES_DB.get(student_id, {})
    subject_lower = subject.lower()

    if subject_lower not in grades:
        raise HTTPException(
            status_code=404,
            detail=f"No '{subject}' grade found. Available: {list(grades.keys())}"
        )

    student_name = STUDENTS_DB[student_id]["name"]
    score = grades[subject_lower]

    return {
        "student": student_name,
        "subject": subject,
        "score": score,
        "grade_letter": "A+" if score >= 95 else "A" if score >= 90 else "B+" if score >= 85 else "B" if score >= 80 else "C" if score >= 70 else "D",
    }


# ============================================================
# 📗 PART 10: Fixed Routes BEFORE Dynamic Routes
# ============================================================
# ⚠️ ORDER MATTERS! Fixed paths must come BEFORE path
# parameters, otherwise FastAPI matches the wrong route.
#
# Try:
#   http://127.0.0.1:8000/items/all       → List all items
#   http://127.0.0.1:8000/items/latest     → Latest item
#   http://127.0.0.1:8000/items/42         → Item #42

ITEMS_DB = {
    1: {"id": 1, "name": "Laptop",   "price": 85000},
    2: {"id": 2, "name": "Mouse",    "price": 500},
    3: {"id": 3, "name": "Keyboard", "price": 1500},
    4: {"id": 4, "name": "Monitor",  "price": 22000},
}

# ✅ Fixed routes FIRST (before the dynamic one)
@app.get("/items/all")
def list_all_items():
    """List ALL items. Fixed route — no path parameter."""
    return {
        "total": len(ITEMS_DB),
        "items": list(ITEMS_DB.values()),
    }

@app.get("/items/latest")
def get_latest_item():
    """Get the latest item. Fixed route — no path parameter."""
    latest_id = max(ITEMS_DB.keys())
    return {"latest": ITEMS_DB[latest_id]}

# ⚠️ Dynamic route AFTER fixed ones
@app.get("/items/{item_id}")
def get_item(item_id: int):
    """Get a specific item by ID. Dynamic route with path parameter."""
    if item_id not in ITEMS_DB:
        raise HTTPException(status_code=404, detail="Item not found")
    return ITEMS_DB[item_id]

# If you put /items/{item_id} BEFORE /items/all:
#   GET /items/all → FastAPI tries to convert "all" to int → 422 ERROR!
# That's why order matters!


# ============================================================
# 📗 PART 11: Root Endpoint & Summary
# ============================================================
# A welcome endpoint that lists all available routes.

@app.get("/")
def root():
    """
    Welcome page — lists all available endpoints to try.
    """
    return {
        "message": "📘 Path Parameters Lesson — FastAPI",
        "instructions": "Visit /docs for interactive Swagger UI",
        "try_these_urls": [
            "/hello/Amitesh",
            "/square/7",
            "/temperature/36.6",
            "/students/1",
            "/students/1/profile",
            "/students/1/grades/math",
            "/courses/python",
            "/math/add/10/5",
            "/math/multiply/3/7",
            "/items/all",
            "/items/latest",
            "/items/1",
        ],
    }


# ============================================================
# 📗 HOW TO RUN THIS LESSON
# ============================================================
#
# 1. Open terminal and navigate to this folder:
#      cd 11_database_and_api
#
# 2. Start the server:
#      python3 -m uvicorn 02_path_parameters:app --reload
#
# 3. Open browser and go to:
#      http://127.0.0.1:8000/docs     ← Swagger UI (try all endpoints!)
#      http://127.0.0.1:8000/          ← Welcome page
#
# 4. Try the URLs from each PART above!
#
# 5. Press Ctrl+C in terminal to stop the server.
#
# ============================================================
# 🏋️ PRACTICE:
# ============================================================
# 1. Add a /users/{user_id} endpoint with your own users dict
# 2. Create /products/{category}/{product_id} with nested params
# 3. Build a /convert/currency/{amount}/{from_curr}/{to_curr}
#    endpoint that converts between USD, EUR, INR
# 4. Add a /students/{id}/grades/average endpoint that
#    returns only the average grade for a student
# 5. Create /fibonacci/{n} that returns the nth fibonacci number
# ============================================================

Continue learning at: https://fastapi.tiangolo.com/tutorial/bigger-applications/#path-operations-with-apirouter


```bash
fastapi dev main.py
```
```
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── items.py
│   │   └── users.py
│   └── internal
│       ├── __init__.py
│       └── admin.py
```

There are several __init__.py files: one in each directory or subdirectory.

This is what allows importing code from one file into another.

For example, in app/main.py you could have a line like:

```python
from app.routers import items
```

---
FastAPI is a modern, fast (hence the name), web framework for building APIs with Python. It is designed for building high-performance applications and offers great support for automatic validation, interactive documentation, and asynchronous programming. Below is a comprehensive guide to its features and uses:

---

## **Core Features**
1. **High Performance**:
   - FastAPI is built on **Starlette** for the web framework core and **Pydantic** for data validation, making it highly efficient and fast.

2. **Automatic Interactive Documentation**:
   - It provides auto-generated interactive API documentation using **Swagger UI** and **ReDoc**.

3. **Type Hints and Validation**:
   - It relies on Python type hints to perform request validation and response serialization automatically.

4. **Asynchronous Programming**:
   - Supports `async` and `await` for handling asynchronous I/O operations, which is great for building APIs that handle many concurrent requests.

5. **Dependency Injection**:
   - FastAPI has a built-in dependency injection system to manage dependencies effectively.

---

## **Getting Started**

### **Installation**
```bash
pip install fastapi[all]
```
- `[all]` installs additional dependencies like `uvicorn` for the ASGI server.

---

### **Basic Example**
A minimal FastAPI application looks like this:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}
```

Run the application with **Uvicorn**:
```bash
uvicorn main:app --reload
```
- Access the interactive docs at `http://127.0.0.1:8000/docs`.

---

## **Features in Detail**

### **Path Parameters**
You can define path parameters directly in the function signature:
```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

### **Query Parameters**
Query parameters are optional and are added as function arguments with default values:
```python
@app.get("/search/")
def search_items(query: str = "default", limit: int = 10):
    return {"query": query, "limit": limit}
```

### **Request Body**
Use Pydantic models to define and validate request payloads:
```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    is_offer: bool = False

@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price}
```

### **Response Models**
Define response models using Pydantic to ensure consistent API responses:
```python
class ResponseModel(BaseModel):
    name: str
    price: float

@app.get("/item/{item_id}", response_model=ResponseModel)
def get_item(item_id: int):
    return {"name": "Sample Item", "price": 25.5}
```

---

## **Advanced Features**

### **Middleware**
Middleware can modify requests and responses globally:
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### **Dependency Injection**
Define reusable dependencies:
```python
from fastapi import Depends

def common_dependency():
    return {"dependency": "value"}

@app.get("/with-dependency/")
def with_dependency(data=Depends(common_dependency)):
    return data
```

### **Background Tasks**
Run tasks in the background:
```python
from fastapi import BackgroundTasks

def write_log(message: str):
    with open("log.txt", "a") as f:
        f.write(message + "\n")

@app.post("/log/")
def log_message(message: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, message)
    return {"message": "Task added"}
```

---

## **Interactive Documentation**

FastAPI automatically generates:
1. **Swagger UI** at `/docs`.
2. **ReDoc** at `/redoc`.

You can customize these as needed.

---

## **Pros and Use Cases**

### **Advantages**
- Simple syntax with Python type hints.
- Excellent performance and scalability.
- Built-in validation and serialization.
- Asynchronous support for handling concurrent requests.

### **Ideal Use Cases**
- Building RESTful APIs.
- Microservices.
- Real-time applications (with WebSockets).
- High-performance applications.

---

FastAPI is widely adopted due to its performance, ease of use, and modern approach to API development. It is especially well-suited for developers familiar with Python who want to build robust, scalable, and well-documented APIs.
---

## **If the Issue Persists**

Run Uvicorn with detailed error logs for more information:
```bash
uvicorn main:app --reload --log-level debug
```

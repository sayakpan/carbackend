# 🚗 Car API with Token Authentication

A simple Django REST API that supports listing and adding car records with token-based user authentication.

---

## 🔧 Tech Used

- Python 3.x  
- Django  
- Django REST Framework  
- Token Authentication (`rest_framework.authtoken`)  
- SQLite (default, easily swappable)  

---

## 🚀 How to Run

### 1. Clone the repo

```bash
git clone https://github.com/sayakpan/carbackend.git
cd carbackend
```

### 2. Create virtual environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create superuser (for admin access)

```bash
python manage.py createsuperuser
```

### 6. Run server

```bash
python manage.py runserver
```

---

## 🔐 Login & Token Process

### ➤ Register a User

```http
POST /api/auth/register/
Content-Type: application/json

{
  "username": "john",
  "password": "pass1234"
}
```

### ➤ Login to get Token

```http
POST /api/auth/login/
Content-Type: application/json

{
  "username": "john",
  "password": "pass1234"
}
```

### ➤ Token Response

```json
{
  "token": "d71330961e3b34706ad734e35922c5cbfca5604f"
}
```

Use this token in the request headers:

```
Authorization: Token d71330961e3b34706ad734e35922c5cbfca5604f
```

---

## 📡 API Endpoints

### 🔹 GET `/api/cars/` – List Cars (paginated)

```http
GET /api/cars/
```

#### Sample Response

```json
{
  "count": 50,
  "next": "http://127.0.0.1:8000/api/cars/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "brand": "Mahindra",
      "model": "Thar",
      "year": 2023,
      "fuel_type": "Petrol",
      "price": 1549000,
      "status": "available"
    }
  ]
}
```

---

### 🔹 POST `/api/cars/` – Add Car (requires token)

```http
POST /api/cars/
Authorization: Token your_token_here
Content-Type: application/json

{
  "brand": "Hyundai",
  "model": "Creta",
  "year": 2024,
  "fuel_type": "Petrol",
  "price": 1200000,
  "status": "available"
}
```

#### Validation Example

```json
{
  "year": ["Year must be a 4-digit number."]
}
```

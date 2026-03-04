# Task Manager API

A RESTful Task Manager API built using Django REST Framework and MySQL.
This API allows users to register, authenticate using JWT, and perform CRUD operations on tasks.

---

## 🚀 Features

- User Registration
- JWT Authentication (Login / Refresh Token)
- Create, Read, Update, Delete Tasks
- Pagination
- Filtering (by completed status)
- Object-level permissions (Users can only manage their own tasks)
- Swagger API Documentation
- Unit Testing

---

## 🛠 Tech Stack

- Python 3.x
- Django
- Django REST Framework
- MySQL
- Simple JWT
- drf-yasg (Swagger)

---

## 📂 Project Structure

task_manager/
│
├── config/ # Project settings
├── tasks/ # Main app
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── permissions.py
│ ├── tests.py
│ └── urls.py
│
├── manage.py
├── requirements.txt
└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
git clone <your-repo-link>
cd task_manager


---

### 2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate # macOS/Linux
venv\Scripts\activate # Windows


---

### 3️⃣ Install Dependencies
pip install -r requirements.txt


---

### 4️⃣ Configure MySQL Database

Create a MySQL database:
CREATE DATABASE task_manager;


Update `config/settings.py` with your database credentials:

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql',
'NAME': 'task_manager',
'USER': 'root',
'PASSWORD': 'your_password',
'HOST': 'localhost',
'PORT': '3306',
}
}


---

### 5️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate


---

### 6️⃣ Create Superuser (Optional)
python manage.py createsuperuser


---

### 7️⃣ Run Development Server
python manage.py runserver


Server will run at:
http://127.0.0.1:8000/


---

## 🔐 Authentication

This project uses JWT Authentication.

### Register User

POST `/api/register/`

{
"username": "testuser",
"password": "password123"
}


---

### Login

POST `/api/login/`


{
"username": "testuser",
"password": "password123"
}


Response:
{
"access": "your_access_token",
"refresh": "your_refresh_token"
}


---

### Use Token

Add this header in all protected requests:


---

## 📌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|------------|
| GET | /api/tasks/ | List all tasks (Authenticated user only) |
| GET | /api/tasks/{id}/ | Retrieve single task |
| POST | /api/tasks/ | Create task |
| PUT | /api/tasks/{id}/ | Update task |
| DELETE | /api/tasks/{id}/ | Delete task |

---

## 🔎 Filtering

Filter tasks by completion status:
GET /api/tasks/?completed=true


---

## 📄 Pagination

Default page size: 5
GET /api/tasks/?page=2


---

## 📚 API Documentation

Swagger documentation available at:

http://127.0.0.1:8000/swagger/


---

## 🧪 Running Tests

Run tests using:
python manage.py test


---

## 🔒 Permissions

- Only authenticated users can create, update, or delete tasks.
- Users can only access their own tasks.
- Object-level permission ensures task ownership validation.

---

## 🧠 Design Decisions

- Used ViewSets to reduce repetitive CRUD code.
- Implemented JWT for stateless authentication.
- Added object-level permissions for security.
- Applied pagination for scalability.
- Used filtering for better usability.

---

## 🚀 Future Improvements

- Role-based access (Admin / User)
- Docker support
- CI/CD integration
- Rate limiting
- API versioning

---

## 👨‍💻 Author

Kanishk Dixit  
Backend Developer (Django | REST APIs | MySQL)

<div align="center">

# 🚀 Production Ready API

### A Production-Grade Backend API built with FastAPI

A clean, modular and scalable backend project implementing modern backend engineering practices including authentication, middleware, logging, testing and Dockerized deployment.

<br>

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-009688?style=for-the-badge&logo=fastapi)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker)
![JWT](https://img.shields.io/badge/Auth-JWT-success?style=for-the-badge)
![Pytest](https://img.shields.io/badge/Tested-Pytest-0A9EDC?style=for-the-badge)

</div>

---

# 📖 Overview

This project was built to practice **production-style backend development** rather than creating a simple CRUD application.

It follows a clean modular architecture and includes many features commonly found in real-world backend systems, including secure authentication, centralized logging, middleware, exception handling, automated testing and Docker support.

---

# ✨ Features

- 🔐 JWT Authentication
- 🔑 Secure Password Hashing
- 👤 User Registration & Login
- 🛡 Protected Endpoints
- 📦 SQLAlchemy ORM
- 🗄 SQLite Database
- ⚙ Environment Variables
- 📝 Centralized Logging
- 🚦 Custom Request Middleware
- ❌ Global Exception Handling
- ❤️ Health Check Endpoint
- 🧪 Automated API Testing
- 🐳 Dockerized Deployment
- 📂 Clean Project Architecture

---

# 🏗 Project Architecture

```
Client
   │
   ▼
Middleware
   │
   ▼
Router
   │
   ▼
Controller
   │
   ▼
Authentication
   │
   ▼
Database
   │
   ▼
Response
```

---

# 📁 Folder Structure

```
Production-Ready-API
│
├── src
│   ├── auth
│   ├── users
│   ├── middleware
│   ├── exceptions
│   ├── database
│   ├── core
│   ├── services
│   └── utils
│
├── tests
├── logs
├── Dockerfile
├── requirements.txt
├── pytest.ini
├── main.py
└── README.md
```

---

# 📂 Module Responsibilities

| Folder | Responsibility |
|----------|---------------|
| auth | Authentication, JWT, Security |
| users | User CRUD Operations |
| middleware | Request Logging |
| exceptions | Custom Exceptions & Global Handlers |
| database | SQLAlchemy Engine & Sessions |
| core | Logging & Application Lifespan |
| utils | Application Settings |
| services | Reserved for Future Business Logic |
| tests | API Testing |

---

# ⚙ Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python 3.14 |
| Framework | FastAPI |
| ORM | SQLAlchemy |
| Database | SQLite |
| Authentication | JWT |
| Validation | Pydantic v2 |
| Password Hashing | pwdlib |
| Logging | Loguru |
| Testing | Pytest |
| Containerization | Docker |

---

# 🔐 Authentication Flow

```
Register
    │
    ▼
Hash Password
    │
    ▼
Store User
    │
    ▼
Login
    │
    ▼
Verify Password
    │
    ▼
Generate JWT
    │
    ▼
Authorization Header
    │
    ▼
Protected Route
```

---

# 🌐 API Endpoints

## Authentication

| Method | Endpoint | Description |
|----------|----------|-------------|
| POST | `/auth/login` | Login & Generate JWT |
| GET | `/auth/me` | Get Current User |

---

## Users

| Method | Endpoint |
|----------|----------|
| POST | `/users` |
| GET | `/users` |
| GET | `/users/{username}` |
| PUT | `/users/{username}` |
| DELETE | `/users/{username}` |

---

## Utility

| Method | Endpoint |
|----------|----------|
| GET | `/health` |

---

# 🐳 Docker

## Build

```bash
docker build -t production-ready-api .
```

## Run

```bash
docker run -d \
--name production-api \
--env-file .env \
-v "$(pwd)/production.db:/app/production.db" \
-p 8000:8000 \
production-ready-api
```

---

# 💻 Local Setup

Clone repository

```bash
git clone https://github.com/whoismehfooz/Production-Ready-API.git
```

Move into project

```bash
cd Production-Ready-API
```

Create Virtual Environment

```bash
python -m venv venv
```

Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Create `.env`

```env
DB_CONNECTION=sqlite:///./production.db
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Run

```bash
uvicorn main:app --reload
```

---

# 🧪 Running Tests

```bash
pytest -v
```

---

# 📈 Project Highlights

✔ Clean Modular Architecture

✔ JWT Authentication

✔ Dependency Injection

✔ SQLAlchemy ORM

✔ Middleware

✔ Centralized Logging

✔ Exception Handling

✔ Docker Support

✔ Automated Testing

✔ Environment-based Configuration

---

# 📚 Key Learning Outcomes

This project provided hands-on experience with:

- FastAPI
- SQLAlchemy ORM
- JWT Authentication
- Password Hashing
- Docker
- Pytest
- Logging
- Middleware
- Dependency Injection
- Clean Architecture
- Linux
- Backend Debugging

---

# 🚀 Future Improvements

- PostgreSQL
- Alembic Migrations
- Docker Compose
- Redis Integration
- Background Tasks
- Refresh Tokens
- Role-Based Access Control (RBAC)
- CI/CD using GitHub Actions
- API Versioning

---

# 👨‍💻 Author

## Mehfooz

Python Backend Developer

GitHub

https://github.com/whoismehfooz

---

<div align="center">

### ⭐ If you found this project interesting, consider giving it a Star!

</div>
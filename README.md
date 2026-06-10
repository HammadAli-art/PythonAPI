# 🐍 PythonAPI

![Python](https://img.shields.io/badge/🔥_PYTHON-3776AB?style=flat-square&logoColor=white)
![last commit](https://img.shields.io/github/last-commit/HammadAli-art/PythonAPI?label=last%20commit&style=flat-square&color=orange)
![Status](https://img.shields.io/badge/Status-Active_Development-brightgreen?style=flat-square)
![REST API](https://img.shields.io/badge/REST-API-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

> 📅 Started: June 2026 — A fully functional REST API built with Django REST Framework supporting complete CRUD operations.

---

## 👋 About This Repo

I built this API from scratch using **Django REST Framework** — each app contains models, serializers, views, and tests for real-world REST API patterns.

---

## 📁 Structure

```
PythonAPI/
├── core/                  # Project settings & root URLs
├── api/                   # Main API app (models, views, serializers)
├── requirements.txt
├── manage.py
└── .env.example
```

---

## 📚 Endpoints Covered So Far

| # | Endpoint | Method | Status |
|---|----------|--------|--------|
| 1 | `/api/items/` | `GET` - List All | ✅ Done |
| 2 | `/api/items/` | `POST` - Create | ✅ Done |
| 3 | `/api/items/{id}/` | `GET` - Retrieve | ✅ Done |
| 4 | `/api/items/{id}/` | `PUT` - Full Update | ✅ Done |
| 5 | `/api/items/{id}/` | `PATCH` - Partial Update | ✅ Done |
| 6 | `/api/items/{id}/` | `DELETE` - Delete | ✅ Done |
| 7 | `/api/auth/token/` | `POST` - Get Token | ✅ Done |

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|------------|
| 🐍 Language | Python 3.11+ |
| 🌐 Framework | Django 4.x |
| 📡 API Layer | Django REST Framework 3.x |
| 🗄️ Database | PostgreSQL / SQLite |
| 🔐 Auth | DRF Token Auth / JWT |
| 🧪 Testing | pytest + Django TestCase |

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> Made with ❤️ using Python & Django REST Framework

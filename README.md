# Yelp Big Data Analysis - Text-to-SQL API

A team project that converts natural language questions into SQL queries and executes them on a PostgreSQL database containing Yelp business data.

## 📋 Overview

This API uses OpenAI's language models to automatically generate and execute SQL queries based on user questions, eliminating the need to write SQL manually.

## 🛠️ My Contribution

- **Database Layer**: Connection pooling and query execution
- **API Schemas**: Request/response validation using Pydantic
- **Core Infrastructure**: FastAPI setup and routing

## 🏗️ Project Structure

```
app/
├── main.py              # FastAPI application
├── api/routes.py        # API endpoints
├── core/                # Configuration & OpenAI integration
├── db/database.py       # Database connection pooling
├── schemas/query.py     # Request/response models
└── services/query_service.py  # Query execution
```

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Environment Variables
```bash
cp .env.example .env
# Add your OpenAI API key and database credentials
```

### 3. Run the Server
```bash
uvicorn app.main:app --reload
```

Server runs at: `http://localhost:8000`

## 📡 API Usage

**Endpoint**: `POST /api/query`

**Request**:
```json
{
  "question": "What are the top 5 highest-rated restaurants?"
}
```

**Response**:
```json
{
  "sql": "SELECT name, stars FROM business_small ORDER BY stars DESC LIMIT 5;",
  "rows": [
    {"name": "Restaurant A", "stars": 4.9},
    {"name": "Restaurant B", "stars": 4.8}
  ]
}
```

## 🔒 Security

- SQL injection prevention (forbidden keywords check)
- Input validation with Pydantic
- SELECT-only queries
- CORS protection

## 💾 Key Components

### Database Connection (`app/db/database.py`)
- Connection pooling for efficient resource management
- Min 1, Max 5 concurrent connections
- Automatic connection cleanup

### Schemas (`app/schemas/query.py`)
- `QueryRequest`: Natural language question input
- `QueryResponse`: SQL + results output
- `ErrorResponse`: Error messages

## 📦 Tech Stack

- FastAPI 0.135.2
- PostgreSQL (psycopg2)
- OpenAI API
- Pydantic 2.12.5

## 📝 Environment Variables

```
OPENAI_API_KEY=your_key_here
DB_HOST=localhost
DB_PORT=5432
DB_NAME=yelp
DB_USER=postgres
DB_PASSWORD=your_password
```

## ✨ Features

✅ Natural language to SQL conversion
✅ Automatic query execution
✅ SQL injection protection
✅ Connection pooling
✅ Type-safe request/response handling
✅ Error handling

---

**Team Project** | Student Implementation

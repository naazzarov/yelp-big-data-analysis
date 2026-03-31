# Yelp Big Data Analysis - Text-to-SQL API

A team project that converts natural language questions into SQL queries using OpenAI's language models and executes them against a PostgreSQL database.

## 🎯 Project Overview

This project is part of our big data analysis curriculum and demonstrates:
- Building production-grade REST APIs with FastAPI
- Integrating Large Language Models (LLMs) for natural language processing
- Database connection pooling and management
- Input validation and security best practices
- Schema validation with Pydantic

The application takes a user's natural language question, uses OpenAI's GPT models to generate safe SQL queries, and executes them against a PostgreSQL database containing Yelp data.

## 👥 Team Structure

This is a collaborative project where different team members handle different components:

- **Your Contribution (Database & API Core)**: Database connection management, schemas, and core API infrastructure
- **Other Team Members**: UI/Frontend, data preprocessing, deployment infrastructure

## 🏗️ Architecture

```
┌─────────────┐
│   User      │
│  (Frontend) │
└──────┬──────┘
       │
       ▼
┌─────────────────────────┐
│   FastAPI Application   │
│  - Routes               │
│  - Request Validation   │
│  - Query Execution      │
└──────┬──────────────────┘
       │
       ├─────────────────────────────┐
       │                             │
       ▼                             ▼
┌──────────────────┐        ┌─────────────────┐
│  OpenAI API      │        │  PostgreSQL DB  │
│  - SQL Gen.      │        │  (Connection    │
│  - LLM Prompt    │        │   Pooling)      │
└──────────────────┘        └─────────────────┘
```

## 🔧 Tech Stack

- **Framework**: FastAPI 0.135.2
- **Web Server**: Uvicorn 0.42.0
- **Database**: PostgreSQL (psycopg2)
- **Validation**: Pydantic 2.12.5
- **LLM**: OpenAI API (GPT models)
- **Environment**: Python 3.10+

## 📦 Project Structure

```
yelp-big-data-analysis/
├── app/
│   ├── main.py                 # FastAPI application setup
│   ├── api/
│   │   └── routes.py          # API endpoints & query validation
│   ├── core/
│   │   ├── config.py          # Configuration & environment variables
│   │   └── openai_client.py   # OpenAI integration
│   ├── db/
│   │   └── database.py        # Database connection pooling [YOUR WORK]
│   ├── schemas/
│   │   └── query.py           # Pydantic models for request/response [YOUR WORK]
│   └── services/
│       └── query_service.py   # Database query execution
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
└── README.md                  # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- PostgreSQL database
- OpenAI API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd yelp-big-data-analysis
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```

   Update `.env` with the required credentials (contact team lead for details)

5. **Run the server**
   ```bash
   uvicorn app.main:app --reload
   ```

   The API will be available at `http://localhost:8000`

## 📚 API Usage

### Endpoint: `POST /api/query`

Convert a natural language question into SQL and execute it.

**Request:**
```json
{
  "question": "What are the top 5 highest-rated restaurants?"
}
```

**Response (Success):**
```json
{
  "sql": "SELECT name, rating FROM restaurants ORDER BY rating DESC LIMIT 5;",
  "rows": [
    {"name": "Restaurant A", "rating": 4.9},
    {"name": "Restaurant B", "rating": 4.8}
  ]
}
```

**Response (Error):**
```json
{
  "error": "Query contains forbidden SQL keywords",
  "sql": "DROP TABLE restaurants;"
}
```

## 🔒 Security Features

- **SQL Injection Prevention**: Forbidden keywords detection (DROP, DELETE, UPDATE, INSERT, TRUNCATE, ALTER)
- **Input Validation**: Pydantic schemas validate all requests
- **CORS Middleware**: Controlled cross-origin requests
- **Environment Variables**: Sensitive credentials never hardcoded

## 💾 Database Layer (Your Contribution)

### Connection Pooling (`app/db/database.py`)

The database module implements connection pooling for efficient resource management:

```python
connection_pool = pool.SimpleConnectionPool(
    minconn=1,    # Minimum connections
    maxconn=5,    # Maximum connections
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)
```

**Key Functions:**
- `get_pool()`: Returns the connection pool, creating it if needed
- `get_connection()`: Retrieves a connection from the pool
- `release_connection(conn)`: Returns a connection to the pool

### Request/Response Schemas (`app/schemas/query.py`)

Pydantic models ensure type safety and automatic validation:

```python
class QueryRequest(BaseModel):
    question: str  # User's natural language question

class QueryResponse(BaseModel):
    sql: str  # Generated SQL query
    rows: Optional[List[Dict[str, Any]]] = None  # Query results

class ErrorResponse(BaseModel):
    error: str  # Error message
    sql: str   # The problematic SQL
```

## 🧪 Testing

*(Add test suite information here as it's developed)*

To run tests once implemented:
```bash
pytest tests/
```

## 📝 Development Notes

### What I (Student) Implemented:
1. **Database Connection Management**
   - Implemented connection pooling to handle multiple concurrent requests
   - Proper resource cleanup with connection release

2. **Request/Response Schemas**
   - Designed Pydantic models for type-safe API contracts
   - Handled optional response fields for error cases

3. **API Core Infrastructure**
   - FastAPI application setup with CORS middleware
   - Request routing and integration between components

### How It Works (Data Flow):
1. Frontend sends natural language question
2. API validates request using `QueryRequest` schema
3. OpenAI generates SQL from the question
4. Generated SQL is validated for security
5. Query executes via database layer using connection pooling
6. Results returned in `QueryResponse` schema
7. Client receives formatted JSON response

## 🚧 Future Improvements

- [ ] Add database schema caching for more accurate SQL generation
- [ ] Implement query result pagination
- [ ] Add comprehensive test suite
- [ ] Database query logging and analytics
- [ ] Support for multiple context windows (few-shot learning)
- [ ] Query result formatting and visualization

## 📖 Learning Outcomes

Through this project, we've learned:
- How to build scalable REST APIs with FastAPI
- Database connection pooling best practices
- Integrating external APIs (OpenAI) into applications
- Software architecture and layered design patterns
- Security considerations in API design
- Type validation with Pydantic

## ✅ Checklist for Team

- [x] Database connection pooling implemented
- [x] Request/response schemas defined
- [x] API routes with security validation
- [x] Environment configuration
- [ ] Unit tests written
- [ ] Integration tests written
- [ ] API documentation (Swagger/OpenAPI)
- [ ] Deployment configuration
- [ ] Performance optimization

## 📞 Contact & Support

For questions about specific components:
- Database & API Core: [Your Name]
- [Other team members and their areas]

## 📄 License

This is a student project created for educational purposes.

---

**Created**: 2024 | **Last Updated**: March 2025

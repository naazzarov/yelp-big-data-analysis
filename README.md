# Yelp Big Data Analysis - Text-to-SQL API

This is a team project where we built an API that converts natural language questions into SQL queries and runs them against a PostgreSQL database with Yelp business data.

## What This Is

Basically, instead of writing SQL manually, you can ask questions in plain English and the API will generate and execute the SQL for you. We use OpenAI's language models to do the translation.

## My Part

I worked on:
- Setting up the database connections with connection pooling
- Creating the request/response schemas for validation
- Building the core API infrastructure with FastAPI

## How It's Structured

```
app/
├── main.py              - The main FastAPI app
├── api/routes.py        - Where the endpoints are defined
├── core/                - Config and OpenAI stuff
├── db/database.py       - Database connection management
├── schemas/query.py     - Pydantic models for requests/responses
└── services/query_service.py  - Actually running the queries
```

## Getting Started

First, install the dependencies:
```bash
pip install -r requirements.txt
```

Then copy the example env file and fill in your credentials:
```bash
cp .env.example .env
```

You'll need your OpenAI API key and database details. Ask a team member if you need help setting this up.

Run the server:
```bash
uvicorn app.main:app --reload
```

It'll be running at http://localhost:8000

## How to Use

Send a POST request to `/api/query` with your question:

```json
{
  "question": "What are the top 5 highest-rated restaurants?"
}
```

You get back the SQL that was generated and the results:

```json
{
  "sql": "SELECT name, stars FROM business_small ORDER BY stars DESC LIMIT 5;",
  "rows": [
    {"name": "Restaurant A", "stars": 4.9},
    {"name": "Restaurant B", "stars": 4.8}
  ]
}
```

## Security Stuff

We made sure to:
- Block dangerous SQL commands (DROP, DELETE, etc)
- Validate all input with Pydantic
- Only allow SELECT queries
- Set up CORS properly

## What We Used

- FastAPI for the API
- PostgreSQL through psycopg2
- OpenAI API for generating SQL
- Pydantic for validation

## The Environment Variables You Need

```
OPENAI_API_KEY=your_actual_key
DB_HOST=localhost
DB_PORT=5432
DB_NAME=yelp
DB_USER=postgres
DB_PASSWORD=your_password
```

## Features

- Natural language to SQL conversion
- Automatic query execution
- Protection against SQL injection
- Connection pooling to handle multiple requests
- Type-safe request/response handling

---

This is a student project done as part of a team.

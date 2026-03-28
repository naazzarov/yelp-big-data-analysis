import re
from fastapi import APIRouter, HTTPException
from app.schemas.query import QueryRequest, QueryResponse, ErrorResponse
from app.core.openai_client import generate_sql
from app.services.query_service import execute_query

router = APIRouter()

FORBIDDEN_KEYWORDS = ["DROP", "DELETE", "UPDATE", "INSERT", "TRUNCATE", "ALTER"]


def is_safe_query(sql: str) -> bool:
    upper_sql = sql.upper()
    return not any(keyword in upper_sql for keyword in FORBIDDEN_KEYWORDS)


def clean_sql(sql: str) -> str:
    sql = re.sub(r"```sql", "", sql)
    sql = re.sub(r"```", "", sql)
    return sql.strip()


@router.post("/query")
async def query(request: QueryRequest):
    sql = generate_sql(request.question)

    print(f"Question: {request.question}")
    print(f"Generated SQL: {sql}")

    sql = clean_sql(sql)

    if not is_safe_query(sql):
        return ErrorResponse(error="Query contains forbidden SQL keywords", sql=sql)

    try:
        rows = execute_query(sql)
        return QueryResponse(sql=sql, rows=rows)
    except ValueError as e:
        return ErrorResponse(error=str(e), sql=sql)
    except Exception as e:
        return ErrorResponse(error=f"Database error: {str(e)}", sql=sql)

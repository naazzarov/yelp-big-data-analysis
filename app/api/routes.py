import re
from fastapi import APIRouter, HTTPException
from app.schemas.query import QueryRequest, QueryResponse
from app.core.openai_client import generate_sql

router = APIRouter()

FORBIDDEN_KEYWORDS = ["DROP", "DELETE", "UPDATE", "INSERT"]


def is_safe_query(sql: str) -> bool:
    upper_sql = sql.upper()
    return not any(keyword in upper_sql for keyword in FORBIDDEN_KEYWORDS)


def clean_sql(sql: str) -> str:
    sql = re.sub(r"```sql", "", sql)
    sql = re.sub(r"```", "", sql)
    return sql.strip()


@router.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest):
    sql = generate_sql(request.question)

    print(f"Question: {request.question}")
    print(f"Generated SQL: {sql}")

    sql = clean_sql(sql)

    if not is_safe_query(sql):
        raise HTTPException(status_code=400, detail="Query contains forbidden SQL keywords")

    return QueryResponse(sql=sql)

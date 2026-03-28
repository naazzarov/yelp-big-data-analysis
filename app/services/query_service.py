import psycopg2.extras
from app.db.database import get_connection, release_connection
from typing import List, Dict, Any

MAX_ROWS = 100


def is_select_query(sql: str) -> bool:
    return sql.strip().upper().startswith("SELECT")


def execute_query(sql: str) -> List[Dict[str, Any]]:
    if not is_select_query(sql):
        raise ValueError("Only SELECT queries are allowed")

    sql = sql.strip()
    if ";" in sql:
        sql = sql.split(";")[0]

    sql = f"{sql} LIMIT {MAX_ROWS}"

    conn = get_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    finally:
        cursor.close()
        release_connection(conn)

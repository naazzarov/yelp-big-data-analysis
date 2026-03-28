from openai import OpenAI
from app.core.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

DB_SCHEMA = """
Table: business_small
Columns:
- business_id (VARCHAR)
- name (VARCHAR)
- city (VARCHAR)
- state (VARCHAR)
- stars (FLOAT)
- review_count (INTEGER)
- categories (VARCHAR)
"""

SYSTEM_PROMPT = f"""You are a SQL expert. Given a natural language question, generate a SQL query.
Database schema:
{DB_SCHEMA}

IMPORTANT:
- ONLY return SQL, no explanation
- Use proper SQL syntax
- Table name is exactly: business_small
- Do NOT include any markdown formatting
"""


def generate_sql(question: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ],
        temperature=0
    )
    return response.choices[0].message.content

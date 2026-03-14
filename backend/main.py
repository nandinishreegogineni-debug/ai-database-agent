from fastapi import FastAPI
import sqlite3
import requests

app = FastAPI()


def generate_sql(question):

    prompt = f"""
You are an AI that converts natural language to SQL.

Database table:
users(id, name, age)

Question: {question}

Return ONLY the SQL query.
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"].strip()


@app.post("/task")
def run_task(data: dict):

    task = data["task"]

    sql = generate_sql(task)

    conn = sqlite3.connect("../database/company.db")
    cursor = conn.cursor()

    cursor.execute(sql)
    result = cursor.fetchall()

    conn.close()

    return {
        "generated_sql": sql,
        "result": result
    }
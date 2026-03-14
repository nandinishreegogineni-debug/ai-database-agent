from fastapi import FastAPI
import sqlite3

app = FastAPI()

def generate_sql(question):
    question = question.lower()

    if "all users" in question:
        return "SELECT * FROM users;"
    
    elif "age" in question:
        return "SELECT name, age FROM users;"
    
    elif "older than 30" in question:
        return "SELECT * FROM users WHERE age > 30;"
    
    else:
        return "SELECT * FROM users;"


@app.post("/task")
def run_task(data: dict):

    task = data["task"]

    sql = generate_sql(task)

    conn = sqlite3.connect("database/company.db")
    cursor = conn.cursor()

    cursor.execute(sql)
    result = cursor.fetchall()

    conn.close()

    return {
        "generated_sql": sql,
        "result": result
    }
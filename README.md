# AI Database Agent

An AI-powered database assistant that converts natural language queries into SQL and retrieves results.

## Tech Stack
- FastAPI
- Streamlit
- SQLite
- Python

## Features
- Natural language to SQL
- FastAPI backend
- Streamlit frontend
- Cloud deployment using Render

## Example Query
Input:
Show all users older than 30

Generated SQL:
SELECT * FROM users WHERE age > 30;

## Deployment
Backend deployed on Render.

## How to Run Locally

Backend:
uvicorn backend.main:app --reload

Frontend:
streamlit run frontend/app.py


App live domain link: https://ai-database-agent-iwrrghznhhumzmyfkz9zzu.streamlit.app/

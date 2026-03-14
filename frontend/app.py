import streamlit as st
import requests

st.title("AI Database Agent")

task = st.text_input("Enter your query")

if st.button("Run"):

    response = requests.post(
        "http://127.0.0.1:8000/task",
        json={"task": task}
    )

    data = response.json()

    st.subheader("Generated SQL")
    st.code(data["generated_sql"])

    st.subheader("Result")
    st.write(data["result"])
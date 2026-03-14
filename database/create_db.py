import sqlite3

conn = sqlite3.connect("company.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

cursor.execute("INSERT INTO users VALUES(1,'Alice',25)")
cursor.execute("INSERT INTO users VALUES(2,'Bob',30)")
cursor.execute("INSERT INTO users VALUES(3,'Charlie',35)")

conn.commit()
conn.close()
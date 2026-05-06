
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://deployment-testing-phase.vercel.app"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB 연결 함수
def get_db():
    return psycopg2.connect(
        host=os.getenv("PGHOST", "localhost"),
        user=os.getenv("PGUSER", "root"),
        password=os.getenv("PGPASSWORD", "1234"),
        database=os.getenv("PGDATABASE", "testdb"),
        port=os.getenv("PGPORT", "5432")
    )

@app.get("/users")
def get_users():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    cursor.close()
    db.close()

    return rows

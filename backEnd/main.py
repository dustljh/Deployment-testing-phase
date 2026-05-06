
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://deployment-testing-phase.vercel.app"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB 연결 함수로 변경 (중요)
def get_db():
    return mysql.connector.connect(
        host=os.getenv("MYSQLHOST", "localhost"),
        user=os.getenv("MYSQLUSER", "root"),
        password=os.getenv("MYSQLPASSWORD", "1234"),
        database=os.getenv("MYSQLDATABASE", "testdb"),
        port=int(os.getenv("MYSQLPORT", "3306"))
    )

@app.get("/users")
def get_users():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()

    cursor.close()
    db.close()

    return result

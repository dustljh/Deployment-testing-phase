

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
import os  # //오류 수정: os 모듈 추가

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # //오류 수정: 개발용 전체 허용
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB 연결 (Railway 환경변수 사용)
db = mysql.connector.connect(
    host=os.getenv("MYSQLHOST"),        # //오류 수정
    user=os.getenv("MYSQLUSER"),        # //오류 수정
    password=os.getenv("MYSQLPASSWORD"),# //오류 수정
    database=os.getenv("MYSQLDATABASE"),# //오류 수정
    port=int(os.getenv("MYSQLPORT","3306"))    # //오류 수정
)

@app.get("/")
def home():
    return {"message": "서버 정상"}

@app.get("/users")
def get_users():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#from fastapi import FastAPI
#from fastapi.middleware.cors import CORSMiddleware
#import mysql.connector
#import os
#app = FastAPI()

# CORS 설정 추가
#app.add_middleware(
 #   CORSMiddleware,
 #   allow_origins=["*"],  # //오류 수정: 모든 출처 허용 (개발용)
 #   allow_methods=["*"],
 #   allow_headers=["*"],
#)

#db = mysql.connector.connect(

 #   host=os.getenv("localhost"),
 #   user=os.getenv("root"),
 #   password=os.getenv("1234"),
 #   database=os.getenv("testdb"),
 #   port=int(os.getenv("3306"))
#)

#@app.get("/users")
#def get_users():
  #  cursor = db.cursor(dictionary=True)
  #  cursor.execute("SELECT * FROM users")
  #  return cursor.fetchall()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # 테스트를 위해 일시적으로 모든 주소 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    name: str
    email: str

db = []

@app.get("/")
def read_root():
    return {"message": "Server is running!"}

@app.post("/users")
def create_user(user: User):
    db.append(user)
    return {"message": "Success", "data": user}

@app.get("/users")
def get_users():
    return db
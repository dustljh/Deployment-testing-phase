from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://deployment-testing-phase.vercel.app",
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    name: str
    email: str

db = []

@app.post("/users")
def create_user(user: User):
    db.append(user)
    return {"message": f"{user.name} 등록 성공!", "data": user}

@app.get("/users", response_model=List[User])
def get_users():
    return db
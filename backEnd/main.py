
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 프론트엔드(Vercel)에서 접속할 수 있도록 허용 (CORS 설정)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # 실제 배포시에는 Vercel 주소만 넣는 것이 안전합니다.
    allow_methods=["*"],
    allow_headers=["*"],
)

# 데이터 모델 정의
class User(BaseModel):
    name: str
    email: str

# 임시 데이터 저장소
db = []

# 1. 데이터 넣기 (POST)
@app.post("/users")
def create_user(user: User):
    db.append(user)
    return {"message": f"{user.name} 등록 성공!", "data": user}

# 2. 데이터 가져오기 (GET)
@app.get("/users", response_model=List[User])
def get_users():
    return db
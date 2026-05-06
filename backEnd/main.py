from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import os

# 데이터베이스 연결을 위한 라이브러리
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
# 1. 데이터베이스 설정
# Render 환경변수에서 DATABASE_URL을 가져옵니다. 
# 없으면 기본적으로 메모리 DB를 사용하도록 설정되어 있습니다.
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 2. DB 테이블 모델 정의 (실제 DB에 생성될 테이블)
class UserTable(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)

# 서버 시작 시 테이블이 없으면 자동으로 생성합니다.
Base.metadata.create_all(bind=engine)

# 3. FastAPI 설정
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 4. 데이터 교환을 위한 Pydantic 모델
class UserSchema(BaseModel):
    name: str
    email: str
    class Config:
        from_attributes = True

# DB 세션을 가져오는 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 5. API 경로 설정
@app.get("/")
def read_root():
    return {"message": "Semicolon Database Server is running!"}

@app.post("/users", response_model=UserSchema)
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    # DB에 새 사용자 저장
    new_user = UserTable(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/users", response_model=List[UserSchema])
def get_users(db: Session = Depends(get_db)):
    # DB에서 모든 사용자 조회
    return db.query(UserTable).all()
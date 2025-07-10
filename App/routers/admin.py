from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.schemas.user import UserCreate
from app.services.user_service import create_user

router = APIRouter()

@router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(SessionLocal)):
    return create_user(db, user)

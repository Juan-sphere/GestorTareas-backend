from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from App.db.database import SessionLocal
from App.schemas.user import UserCreate
from App.services.user_service import create_user

router = APIRouter()

@router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(SessionLocal)):
    return create_user(db, user)

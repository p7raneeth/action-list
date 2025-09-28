from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import createUser
from app.models.users import User
from typing import List
from passlib.context import CryptContext
# from fastapi.security import OAuthPasswordRequestForm, OAuth2PasswordBearer


router = APIRouter(prefix="/user", tags=["user"])

SECRET_KEY = "ILOVETOKYO123098"
ALGORITHM = "HS256"

pwd_hash = CryptContext(schemes=['argon2'], deprecated='auto')


@router.post("/", status_code=200)
def create_user(user: createUser , db: Session = Depends(get_db)):
    user_details = User(
        username = user.username,
        password = pwd_hash.hash(user.password)
    )
    db.add(user_details)
    db.commit()
    db.refresh(user_details)

    return {
        "message" : "new user has been created",
        "user_id" : user_details.id
                }


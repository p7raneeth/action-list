from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import createUser
from app.models.users import User
from typing import List

router = APIRouter(prefix="/user", tags=["user"])

@router.post("/", status_code=200)
def create_user(user : createUser, db: Session = Depends(get_db)):
    user_details = User(
        username = user.username,
        password  = user.password
    )

    db.add(user_details)
    db.commit()
    db.refresh(user_details)

    return {
        "message" : "new user has been created",
        "user_id" : user_details.id
                }
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import createUser, Token
from app.models.user import User
from typing import List, Annotated
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import timedelta, datetime
from jose import jwt, JWTError

router = APIRouter(prefix="/user", tags=["user"])


SECRET_KEY = "ILOVETOKYO123098"
ALGORITHM = "HS256"

pwd_hash = CryptContext(schemes=['argon2'], deprecated='auto')
# oauth2_bearer = OAuth2PasswordBearer(tokenUrl='/token')

@router.post("/", status_code=201)
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

@router.post("/token", response_model=Token)
def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],  db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='user could not be found')
    token = create_access_token(user.username, user.id, timedelta(minutes=20))
    return {'access_token': token, 'token_type':'bearer'}

def create_access_token(username:str, user_id:str, expires:timedelta):
    encode = {'sub': username, 'id':user_id}
    expires = datetime.utcnow() + expires
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

def authenticate_user(username:str, password:str, db):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not pwd_hash.verify(password, user.password):
        return False
    return user


    


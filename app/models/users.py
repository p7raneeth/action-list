from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, JSON, Date
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password_hashed = Column(String)
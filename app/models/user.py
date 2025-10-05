from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, JSON, Date
# from sqlalchemy.ext.declarative import declarative_base
from app.database import Base 
from sqlalchemy.orm import relationship

# Base = declarative_base()
# metadata = Base.metadata

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String, unique=True)

    # ⚠️ Make sure this line exists!
    tasks = relationship("Task", back_populates="user")
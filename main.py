from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from typing import Annotated
from sqlalchemy.orm import Session
from app.database import get_db
from app.routers.auth import get_current_user
from app.models import Base, User, Task  # Import all models together
from app.database import engine

# Create tables
Base.metadata.create_all(bind=engine)

from app.routers import tasks, user, auth


# Create FastAPI app
app = FastAPI(
    title="Task Management API",
    description="A simple task management API",
    version="1.0.0"
)

# Include the tasks router
app.include_router(tasks.router, prefix="/api/v1")
app.include_router(user.router, prefix="/api/v1")
app.include_router(auth.router, prefix="/api/v1")

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Task Management API is running!"}

# Health check
@app.get("/health")
def health_check():
    return {"status": "healthy"}
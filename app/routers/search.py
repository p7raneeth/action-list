from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.tasks import TaskCreate, TaskResponse, TaskUpdate
from app.models.tasks import Task
from typing import List

router = APIRouter(prefix="/search", tags=["search"])




@router.get("/{key_word}", response_model=TaskResponse)
def search(task_id: int, db:Session=Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


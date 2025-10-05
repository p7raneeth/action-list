from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.tasks import TaskCreate, TaskResponse, TaskUpdate
# from app.models.tasks import Task
# from app.models.user import User
from app.routers.auth import get_current_user
from typing import List, Annotated

# In routers/tasks.py
from app.models import Task, User


router = APIRouter(prefix="/tasks", tags=["tasks"])
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[User, Depends(get_current_user)]


@router.post("/", status_code=201)
def create_task(task: TaskCreate, current_user: user_dependency,  db: Session = Depends(get_db)):
    """Create a new task"""
    # Create new task instance
    new_task = Task(
        title=task.title,
        description=task.description,
        priority=task.priority,
        due_date=task.due_date,
        tags=task.tags,
        completed=False,  # Always start as not completed
        user_id = current_user.id)
    # Add to database
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {
        "message": "Task created successfully",
        "task_id": new_task.id   }


@router.get("/", response_model=List[TaskResponse])
def fetch_all_tasks(current_user: user_dependency, db: Session = Depends(get_db)):
    # tasks = db.query(Task).order_by(Task.created_at.desc()).all()
    tasks = db.query(Task).filter(Task.user_id == current_user.id).order_by(Task.created_at.desc()).all()
    print('tasks', tasks)
    return tasks


@router.get("/{task_id}", response_model=TaskResponse)
def fetch_task_by_id(task_id: int, current_user: user_dependency,  db:Session=Depends(get_db)):
    # task = db.query(Task).filter(Task.id == task_id).first()
    task = db.query(Task).filter(Task.user_id == current_user.id).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=TaskResponse)
def update_task_by_id(task_update:TaskUpdate, current_user: user_dependency, task_id: int, db:Session=Depends(get_db)):
    # task = db.query(Task).filter(Task.id == task_id).first()
    task = db.query(Task).filter(Task.user_id == current_user.id).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    update_data = task_update.dict(exclude_unset=True)
    for f,v in update_data.items():
        setattr(task, f, v)
    db.commit()
    db.refresh(task)
    return task

@router.delete("/{task_id}", response_model = {})
def delete_task_by_id(task_id: int, current_user: user_dependency,  db:Session=Depends(get_db)):
    # task = db.query(Task).filter(Task.id == task_id).first()
    task = db.query(Task).filter(Task.user_id == current_user.id).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task already deleted")
    db.delete(task)
    db.commit()
    return {
        "message": "Task deleted successfully",
        "task_id": task.id
    }

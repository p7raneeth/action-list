from sqlalchemy.orm import Session
from app.models import tasks
from sqlalchemy import func

from app.schemas import tasks


def get_task(db: Session, task_id: int):
    return db.query(tasks.Task).filter(tasks.Task.id == task_id).first()

def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(tasks.Task).offset(skip).limit(limit).all()

def create_task(db: Session, task: tasks.TaskCreate):
    db_task = tasks.Task(
    title=task.title,
    description=task.description
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, task: tasks.TaskUpdate):
    db_task = get_task(db, task_id)
    if db_task:
        for key, value in task.dict(exclude_unset=True).items():
            setattr(db_task, key, value)
        db.commit()
        db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int):
    db_task = get_task(db, task_id)
    if db_task:
        db.delete(db_task)
        db.commit()
    return db_task

from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from enum import Enum

class PriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class TaskCreate(BaseModel):
    title : str
    description : str
    priority : PriorityEnum = PriorityEnum.medium
    due_date : datetime
    tags : Optional[List[str]] = []

class TaskResponse(BaseModel):
    id : int
    title : str
    description : str
    completed : bool
    priority : PriorityEnum
    due_date : datetime
    tags : List[str]
    created_at : datetime
    updated_at : datetime

    class Config:
        from_attributes = True

class TaskUpdate(BaseModel):
    id : Optional[int] = None
    title : Optional[str] = None
    description : Optional[str] = None
    completed : Optional[bool] = None
    priority : Optional[PriorityEnum] = None
    due_date : Optional[datetime] = None
    tags : Optional[List[str]] = None

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TaskCreate(BaseModel):
    user_id: int
    title: str
    priority: str
    duration: int
    deadline: datetime
    type: str

class Task(TaskCreate):
    id: int
    completed: bool

    class Config:
        from_attributes = True

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from .database import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    title = Column(String, index=True)
    priority = Column(String)
    duration = Column(Integer)
    deadline = Column(DateTime)
    type = Column(String)
    completed = Column(Boolean, default=False)

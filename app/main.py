from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/add-task")
def add_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@app.get("/get-tasks/{user_id}")
def get_tasks(user_id: int, db: Session = Depends(get_db)):
    return crud.get_tasks(db, user_id)

@app.post("/sync-calendar")
def sync_calendar():
    """Stub endpoint for syncing with Apple Calendar (to be implemented)."""
    return {"message": "Calendar sync feature coming soon."}

@app.post("/schedule-tasks")
def schedule_tasks():
    """Stub endpoint for scheduling tasks (to be implemented)."""
    return {"message": "Task scheduling feature coming soon."}

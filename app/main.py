from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI-Powered Calendar Assistant", version="1.0.0")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    """Welcome message for the API"""
    return {"message": "Welcome to AI-Powered Calendar Assistant API", "version": "1.0.0"}

@app.post("/add-task", response_model=schemas.Task)
def add_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    """Add a new task to the database"""
    return crud.create_task(db, task)

@app.get("/get-tasks/{user_id}", response_model=list[schemas.Task])
def get_tasks(user_id: int, db: Session = Depends(get_db)):
    """Get all tasks for a specific user"""
    return crud.get_tasks(db, user_id)

@app.put("/update-task/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, task_update: schemas.TaskCreate, db: Session = Depends(get_db)):
    """Update an existing task"""
    updated_task = crud.update_task(db, task_id, task_update)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@app.delete("/delete-task/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """Delete a task"""
    success = crud.delete_task(db, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}

@app.patch("/complete-task/{task_id}", response_model=schemas.Task)
def complete_task(task_id: int, db: Session = Depends(get_db)):
    """Mark a task as completed"""
    task = crud.mark_task_complete(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.post("/sync-calendar")
def sync_calendar():
    """Stub endpoint for syncing with Apple Calendar (to be implemented)."""
    return {"message": "Calendar sync feature coming soon."}

@app.post("/schedule-tasks")
def schedule_tasks():
    """Stub endpoint for scheduling tasks (to be implemented)."""
    return {"message": "Task scheduling feature coming soon."}

from fastapi import APIRouter, HTTPException, status
from typing import List
from uuid import UUID, uuid4
from datetime import datetime
from app.data import db
from app.schemas import Task, TaskCreate, TaskUpdate

router = APIRouter()


@router.get("/tasks", response_model=List[Task])
def read_tasks():
    return list(db.values())


@router.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: UUID):
    task = db.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_in: TaskCreate):
    tid = uuid4()
    task = Task(id=tid, created_at=datetime.utcnow(), **task_in.dict())
    db[tid] = task
    return task


@router.put("/tasks/{task_id}", response_model=Task)
def replace_task(task_id: UUID, task_in: TaskCreate):
    existing = db.get(task_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Task not found")
    task = Task(id=task_id, created_at=existing.created_at, **task_in.dict())
    db[task_id] = task
    return task


@router.patch("/tasks/{task_id}", response_model=Task)
def update_task(task_id: UUID, task_in: TaskUpdate):
    existing = db.get(task_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Task not found")
    updated = existing.copy(update=task_in.dict(exclude_unset=True))
    db[task_id] = updated
    return updated


@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: UUID):
    deleted = db.pop(task_id, None)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return

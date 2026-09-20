from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

from app.services.database import get_db

router = APIRouter()

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    created_at: datetime

    class Config:
        from_attributes = True

@router.get('/tasks', response_model=List[TaskResponse])
async def list_tasks(db: AsyncSession = Depends(get_db)):
    return []

@router.post('/tasks', response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskCreate, db: AsyncSession = Depends(get_db)):
    return TaskResponse(id=1, title=task.title, description=task.description, completed=False, created_at=datetime.now())
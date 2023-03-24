from typing import List
from pydantic import BaseModel

from models.resources import Resource

class LessonBase(BaseModel):
    name: str
    description: str

class LessonCreate(LessonBase):
    pass

class Lesson(LessonBase):
    id: int
    resources: List[Resource] = []

    class Config:
        orm_mode = True
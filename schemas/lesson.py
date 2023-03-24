from typing import List
from pydantic import BaseModel


class LessonBase(BaseModel):
    name: str
    description: str

class LessonCreate(LessonBase):
    pass

class Lesson(LessonBase):
    id: int

    class Config:
        orm_mode = True
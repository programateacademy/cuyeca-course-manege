from typing import List, Optional
from models.resources import Resource
from pydantic import BaseModel, Field, validator

class LessonBase(BaseModel):
    name: str
    description: str = None
    resources: Optional[List[Resource]] = None

class LessonCreate(LessonBase):
    pass

class Lesson(LessonBase):
    id: int

    class Config:
        orm_mode = True

    @validator('resources', each_item=True)
    def validate_resource(cls, value):
        if not isinstance(value, Resource):
            raise ValueError('Resources must be of type Resource')
        return value

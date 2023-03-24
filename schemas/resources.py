from typing import List
from pydantic import BaseModel

class ResourceBase(BaseModel):
    file_path: str

class ResourceCreate(ResourceBase):
    pass

class Resource(ResourceBase):
    id: int
    lesson_id: int

    class Config:
        orm_mode = True
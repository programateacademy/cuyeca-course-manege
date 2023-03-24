from pydantic import BaseModel, Field
from typing import Optional

class ResourceBase(BaseModel):

    name: str = Field(max_length=100, min_length=10)
    description: str = Field(max_length=1000, min_length=10)
    path_resource: str = Field(max_length=100, min_length=10)
    resource_id: Optional[int] = None

class ResourceCreate(ResourceBase):
    pass

class Resource(ResourceBase):
    id: int

    class Config:
        orm_mode = True
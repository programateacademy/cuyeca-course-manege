# from pydantic import BaseModel, Field, Config
# from typing import List, Optional

# class Resource:
#     def __init__(self, name: str, value: int):
#         self.name = name
#         self.value = value

# class ResourceBase(BaseModel):
#     name: str
#     description: Optional[str] = None

# class Resource(BaseModel):
#     name: str
#     url: str

# class ResourceCreate(ResourceBase):
#     pass

# class Resource(ResourceBase):
#     id: int

#     class Config:
#         arbitrary_types_allowed = True


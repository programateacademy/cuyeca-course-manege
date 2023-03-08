from pydantic import BaseModel, Field

class Admin(BaseModel):
    
    username: str = Field(max_length=15,min_length=5)
    password: str = Field(max_length=10,min_length=8)
    role: str = Field(max_length=10, min_length=4)
    is_superuser: bool = False
    
    class Config:
        schema_extra = {
            "example":{
                 "username": "laura.gonzales",
                 "password": "abcdef ",
                 "role": "admin",
                 "is_superuser":"false",
            }
        }
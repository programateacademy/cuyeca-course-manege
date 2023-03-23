from typing import Optional
from pydantic import BaseModel, Field


class Courses(BaseModel):

    id : Optional[int] = None
    topic: str = Field(max_length=500,min_length=5)
    message: str = Field(max_length=50000,min_length=10)
    

    class Config:
        schema_extra = {
            "example":{
                 "topic": "Derecho de los niños",
                 "message": "es un placer estar aquí para hablar sobre un tema muy importante y sensible: los derechos de los niños. Como sociedad, es nuestro deber proteger y garantizar los derechos de los niños, ya que son los más vulnerables y necesitan nuestro apoyo para crecer y desarrollarse de manera saludable."
                 
            }
        }
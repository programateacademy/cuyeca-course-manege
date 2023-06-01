from typing import List, Optional
from pydantic import BaseModel,Field



class Lesson(BaseModel):
    id : Optional[int] = None
    name: str = Field(max_length=100, min_length=5 )
    description: str = Field(max_length=500, min_length=10 )
    video : str = Field(max_length=100, min_length=5 )
    resources : str = Field(max_length=100, min_length=5 )
   


    class Config:
        schema_extra = {
            "example":{
                "name": "lección 1",
                "description": "esta lección busca ayudar a comprender la realidad social ",
                "video": "https://www.youtube.com/",
                "resources": "https://drive.google.com/drive/folders/1OoXC4Z5_3TIvcXnQm-wYRoHHkYYhUk9A?usp=sharing",
            }
        }



# class LessonCreate(LessonBase):
#     pass

# class Lesson(LessonBase):
#     id: int

#     class Config:
#         orm_mode = True
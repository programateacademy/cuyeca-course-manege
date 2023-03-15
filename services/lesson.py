from operator import and_
from models.lesson import Lesson as LessonModel
from schemas.lesson import Lesson

class LessonService():
    def __init__(self,db)-> None:
        self.db = db

    def get_lesson(self):
        result = self.db.query(LessonModel).all()
        return result
    
    def get_lesson_by_id(self,id:int):
        result = self.db.query(LessonModel).filter(and_(LessonModel.id == id , LessonModel.status == True)).first()
        return result
    
    def get_lesson_by_name(self,name:str):
        result = self.db.query(LessonModel).filter(LessonModel.name == name).first()
        return result
    
    def create_lesson(self,lesson:Lesson):
        new_lesson = LessonModel(
            id= lesson.id,
            name = lesson.name,
            description = lesson.description,
            title_resource = lesson.title_resource,
            resouce = lesson.resource
        )
        self.db.add(new_lesson)
        self.db.commit()
        return
    
def update_lesson(self,id:int, data:Lesson):
    lesson = self.db.query(LessonModel).filter(LessonModel.id == id).first()
    lesson.name = data.name
    lesson.description = data.description
    lesson.title_resource = data.title_resource
    lesson.resource = data.resource
    self.db.commit()
    return

def update_lesson_by_name(self,name:str, data:Lesson):
    lesson = self.db.query(LessonModel).filter(LessonModel.name == name).first()
    lesson.name = data.name
    lesson.description = data.description
    lesson.title_resource = data.title_resource
    lesson.resource = data.resource
    self.db.commit()
    return

def update_status_lesson(self, id:int):
        lesson = self.db.query(LessonModel).filter(LessonModel.id == id).first()
        lesson.status = False
        self.db.commit()
        return

def delete_lesson(self, id:int):
    self.db.query(LessonModel).filter(LessonModel.id == id).delete()
    self.db.commit()
    return

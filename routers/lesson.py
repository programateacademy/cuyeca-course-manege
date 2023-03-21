import shutil
from fastapi import APIRouter, Path, Query, UploadFile, File
from config.database import Session
from models.lesson import Lesson as LessonModel
from schemas.lesson import Lesson
from typing import List
from services.lesson import LessonService
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session

lesson_router = APIRouter()

@lesson_router.get('/lesson', tags=['lesson'], response_model=List[Lesson],status_code=200)
def get_lesson() -> Lesson:
    db = Session()
    result = LessonService(db).get_lesson()
    return JSONResponse (content=jsonable_encoder(result), status_code=200)

@lesson_router.get('/lesson/{id}', tags=['lesson'], response_model=Lesson,status_code=200)
def get_lesson_by_id(id:int = Path(ge=1,le=2000)):
    db = Session()
    result = LessonService(db).get_lesson_by_id(id)
    if not result:
        return JSONResponse(status_code=400, content={"message": "ninguna lección existe con ese id"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@lesson_router.get('/lesson', tags=['lesson'], response_model=Lesson,status_code=200)
def get_lesson_by_name(name:str = Query(min_length=1, max_length=500)):
    db = Session()
    result = db.query(LessonModel).filter(LessonModel.name == name).all()
    if not result:
        return JSONResponse(status_code=400, content={"message": "ninguna lección existe con ese nombre"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@lesson_router.post('/lesson', tags=['lesson'], status_code=200, response_model=dict,)
def create_lesson(lesson: Lesson, file: UploadFile = File(...))->dict:
    with open(f'{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    db = Session()
    LessonService(db).create_lesson(lesson)
    return JSONResponse(content={"message":"Lección creada satisfactoriamente"}, status_code=200)



@lesson_router.put('/lesson/{id}', tags=['lesson'], status_code=200)
def update_lesson(id:int, lesson:Lesson):
    db = Session()
    result = LessonService(db).get_lesson_by_id(id)
    if not result:
        return JSONResponse(content={"message":"Lección no encontrada con ese id"}, status_code=400)
    LessonService(db).update_lesson(id, lesson)
    return JSONResponse(content={"message":"Lección actualizada satisfactoriamente"}, status_code=200)

@lesson_router.put('/lesson/', tags=['lesson'], status_code=200)
def update_lesson_by_name(name:str, lesson:Lesson):
    db = Session()
    result = LessonService(db).get_lesson_by_name(name)
    if not result:
        return JSONResponse(content={"message":"nombre de lección no actualizado"}, status_code=400)
    LessonService(db).update_lesson_by_name(name, lesson)
    return JSONResponse(content={"message":"Nombre de lección actualizado satisfactoriamente"}, status_code=200)


@lesson_router.patch('/lesson/', tags=['lesson'], status_code=200)
def update_status_lesson(id:int):
    db = Session()
    result = LessonService(db).get_lesson_by_id(id)
    print ("Lesson status route")
    if not result:
        return JSONResponse(content={"message":"Lección no encontrada con ese id"}, status_code=400)
    LessonService(db).update_status_lesson(id)
    return JSONResponse(content={"message":"estado de la lección actualizada satisfactoriamente"}, status_code=200)

@lesson_router.delete('/lesson/{id}', tags=['lesson'], status_code=200)
def delete_lesson(id:int) -> dict:
    db = Session()
    result = db.query(LessonModel).filter(LessonModel.id == id).first()
    if not result:
        return JSONResponse(content={"message":"Lección no encontrada con ese id"}, status_code=400)
    LessonService(db).delete_lesson(id)
    return JSONResponse(content={"message":"lección eliminada satisfactoriamente"}, status_code=200)


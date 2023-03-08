from fastapi import APIRouter, HTTPException, status 
from fastapi import APIRouter, Path, Query
from config.database import Session
from models.courses import Courses as CoursesModel 
from schemas.courses import Courses
from typing import List
from services.courses import CoursesService
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder 


courses_router = APIRouter()

@courses_router.get('/courses', tags=['courses'], response_model=List[Courses],status_code=200)
def get_courses() -> Courses:
    db = Session()
    result = CoursesService(db).get_courses()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@courses_router.get('/courses/{id}', tags=['courses'], response_model=Courses, status_code=200)
def get_courses_by_id(id:int = Path(ge=1,le=2000)):
    db = Session()
    result= CoursesService(db).get_courses_by_id(id)
    if not result:
        return JSONResponse(status_code=400, content={"message":"Cursos no encontrado con ese id"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@courses_router.get('/courses/', tags=['courses'], response_model=Courses, status_code=200)
def get_courses_by_name(name:str = Query(min_length=1,max_length=2000)):
    db = Session()
    result= db.query(CoursesModel).filter(CoursesModel.name == name).all()
    if not result:
        return JSONResponse(status_code=400, content={"message":"Cursos no encontrado con ese nombre"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@courses_router.post('/courses', tags=["courses"], status_code=200, response_model=dict)
def create_courses(courses:Courses)->dict:
    db = Session()
    CoursesService(db).create_courses(courses)
    return JSONResponse(content={"message":"Curso creado satisfactoriamente"},status_code=200)

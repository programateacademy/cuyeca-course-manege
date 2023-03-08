from fastapi import FastAPI
from config.database import Session, engine, Base
from middlewares.error_handler import Errorhandler
from routers.courses import courses_router

app = FastAPI()
app.title = "App with fastAPI and react"

app.add_middleware(Errorhandler)
app.include_router(courses_router)


Base.metadata.create_all(bind=engine)


@app.get('/', tags=['home'])
def message(): 
    return "Hello World"

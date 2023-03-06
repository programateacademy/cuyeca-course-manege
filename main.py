from fastapi import FastAPI
from config.database import Session, engine, Base
from middlewares.error_handler import Errorhandler


app = FastAPI()
app.title = "App with fastAPI and react"

app.add_middleware(Errorhandler)
Base.metadata.create_all(bind=engine)


@app.get('/', tags=['home'])
def message(): 
    return "Hello World"

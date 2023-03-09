from fastapi import FastAPI
import fastapi as _fastapi
from config.database import Session, engine, Base
from middlewares.error_handler import Errorhandler
import fastapi.security as _security
import sqlalchemy.orm as _orm
import services.admin as _serviceadmin
import schemas.admin as _schemaadmin


app = FastAPI()
app.title = "App with fastAPI and react"

app.add_middleware(Errorhandler)

Base.metadata.create_all(bind=engine)



@app.get('/', tags=['home'])
def message(): 
    return "Hello World"

@app.post("/api/admin")
async def create_superadmin(superadmin:_schemaadmin.SuperadminCreate,db: _orm.Session = _fastapi.Depends(_serviceadmin.get_db)):
    db_superadmin = await _serviceadmin.get_superadmin_by_email(superadmin.email,db)
    if db_superadmin:
        raise _fastapi.HTTPException(status_code=400, detail= "Email already exists in superadmin")
    return await _serviceadmin.create_superadmin(superadmin,db)



# this is a endpoint to prove react with fastapi
@app.get("/api")
async def root():
    return{"message":"Creación administradores"}
from fastapi import FastAPI
import fastapi as _fastapi
from config.database import Session, engine, Base
from middlewares.error_handler import Errorhandler

from routers.courses import courses_router
import fastapi.security as _security
import sqlalchemy.orm as _orm
import services.admin as _serviceadmin
import schemas.admin as _schemaadmin



app = FastAPI()
app.title = "App with fastAPI and react"

app.add_middleware(Errorhandler)

app.include_router(courses_router)



Base.metadata.create_all(bind=engine)



@app.get('/', tags=['home'])
def message(): 
    return "Hello World"

# endpoint that create a superadmin

@app.post("/api/superadmin")
async def create_superadmin(superadmin:_schemaadmin.SuperadminCreate,db: _orm.Session = _fastapi.Depends(_serviceadmin.get_db)):
    db_superadmin = await _serviceadmin.get_superadmin_by_email(superadmin.email,db)
    if db_superadmin:
        raise _fastapi.HTTPException(status_code=400, detail= "Email already exists in superadmin")
    await _serviceadmin.create_superadmin(superadmin,db)
    
    return await _serviceadmin.create_token(superadmin)

@app.post("/api/token")
async def generate_token(form_data:_security.OAuth2PasswordRequestForm = _fastapi.Depends(),db:_orm.Session = _fastapi.Depends(_serviceadmin.get_db)):
    superadmin = await _serviceadmin.authenticate_superadmin(form_data.username, form_data.password,db)
    
    if not superadmin:
        raise _fastapi.HTTPException(status_code=401, detail="Invalid Credentials")
    
    return await _serviceadmin.create_token(superadmin)

@app.get("/api/superadmin/me", response_model=_schemaadmin.Superadmin)
async def get_superadmin(superadmin: _schemaadmin.Superadmin = _fastapi.Depends(_serviceadmin.get_current_superadmin) ):
    return superadmin  


@app.post("/api/admin", response_model=_schemaadmin.Admin)
async def create_admin(admin: _schemaadmin.Admin, superadmin: _schemaadmin.Superadmin = _fastapi.Depends(_serviceadmin.get_current_superadmin),db:_orm.Session = _fastapi.Depends(_serviceadmin.get_db)):
    pass

# this is a endpoint to prove react with fastapi
@app.get("/api")
async def root():
    return{"message":"Creación administradores"}
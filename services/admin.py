import config.database as _database
import models.admin as _modeladmin
import schemas.admin as _schemaadmin
import sqlalchemy.orm as _orm
import passlib.hash as _hash

def create_database():
    return _database.Base.create_all(bind=_database.engine)

def get_db():
    db = _database.Session()
    try:
        yield db 
    finally:
        db.close()

async def get_superadmin_by_email(email:str, db:_orm.Session):
    return db.query(_modeladmin.Superadmin).filter(_modeladmin.Superadmin.email == email).first()

# function with hash to create password
async def create_superadmin(superadmin:_schemaadmin.SuperadminCreate, db:_orm.Session):
    superadmin_obj = _modeladmin.Superadmin(email=superadmin.email,username=superadmin.username,password=_hash.bcrypt.hash(superadmin.password))
    db.add(superadmin_obj)
    db.commit()
    db.refresh(superadmin_obj)
    return superadmin_obj
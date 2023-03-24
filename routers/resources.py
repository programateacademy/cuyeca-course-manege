# import os
# import schemas
# import models
# from fastapi import FastAPI, HTTPException, File, UploadFile, Depends
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from models.resources import Resource
# from schemas.resources import Resource

# Base = declarative_base()
# resources_router = FastAPI()

# # Configure the database connection
# base_dir = os.path.abspath(os.path.dirname(__file__))
# sqlite_file_name = "mydatabase.db"
# SQLALCHEMY_DATABASE_URL = f"sqlite:///{os.path.join(base_dir,sqlite_file_name)}"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base.metadata.create_all(bind=engine)

# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Resource routes and services
# @resources_router.post("/resources/", response_model=schemas.Resource)
# async def create_resource(resource: schemas.ResourceCreate, db: Session = Depends(get_db)):
#     db_resource = models.Resource(**resource.dict())
#     db.add(db_resource)
#     db.commit()
#     db.refresh(db_resource)
#     return db_resource

# @resources_router.post("/resources/upload/", response_model=schemas.Resource)
# async def create_upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
#     contents = await file.read()
#     db_resource = models.Resource(file_path=file.filename)
#     db.add(db_resource)
#     db.commit()
#     db.refresh(db_resource)
#     return db_resource

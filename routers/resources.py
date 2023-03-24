from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session
from typing import List
from dependencies import get_db
from services.resources import ResourcesService
from schemas.resources import Resources
from models.resources import Resources

resources_router = APIRouter()



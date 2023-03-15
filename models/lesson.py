from sqlalchemy import Column, Integer, String, Boolean
from config.database import Base
from pydantic import UploadFile
class Lesson (Base):
    __tablename__ = "lesson"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    title_resource = Column(String)
    resource = Column(UploadFile[String])
    status = Column(Boolean, default=True)
    




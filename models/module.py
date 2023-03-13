from sqlalchemy import Column, Integer, String, Boolean, Tuple
from config.database import Base

class Lesson (Base):
    __tablename__ = "lesson"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    resource = Column(Tuple[String])
    




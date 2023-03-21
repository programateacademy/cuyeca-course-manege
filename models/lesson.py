from sqlalchemy import BLOB, Column, Integer, String, Boolean, LargeBinary
from config.database import Base


class Lesson (Base):
    __tablename__ = "lesson"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    title_resource = Column(String)
    status = Column(Boolean, default=True)
    




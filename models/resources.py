from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Files(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    path_resource= Column(Integer, ForeignKey('lesson.id'))

    upload = relationship("lesson", back_populates="resource")
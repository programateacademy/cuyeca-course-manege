from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Resource(Base):
    __tablename__ = 'resource'

    id = Column(Integer, primary_key=True, index=True)
    lesson_id = Column(Integer, ForeignKey('lesson.id'))
    file_path = Column(String)

    lesson = relationship('Lesson', back_populates='resources')
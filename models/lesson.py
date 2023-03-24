from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from schemas.lesson import Lesson

Base = declarative_base()

class Lesson(Base):
    __tablename__ = 'lesson'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)

    resources = relationship('Resource', back_populates='lesson')




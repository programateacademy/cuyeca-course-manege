from sqlalchemy import Column, Integer, String

from config.database import Base

class Forum(Base):
    __tablename__ = "forum"

    id = Column(Integer, primary_key=True)
    topic = Column(String)
    message = Column(String)
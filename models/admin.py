from sqlalchemy import Boolean, Column, String
from config.database import Base


class Admin(Base):
    __tablename__='admin'
    username = Column(String(15))
    password = Column(String(10))
    role = Column(String(10))
    is_superuser = Column(Boolean)
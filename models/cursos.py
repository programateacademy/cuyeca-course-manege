from sqlalchemy import Column, Integer, String

from config.database import Base

class Cursos(Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    descripcion = Column(String)
    lineas_de_trabajo = Column(String)
    objetivos_especificos = Column(String)
    tipo_de_curso = Column(String)
    
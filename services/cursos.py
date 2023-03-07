from models.cursos import Cursos as CursosModel
from schemas.cursos import Cursos

class CursosService():
    def __init__(self,db) -> None:
        self.db = db

    def get_cursos(self):
        result = self.db.query(CursosModel).all()
        return result
    
    def get_cursos_by_id(self, id:int):
        result = self.db.query(CursosModel).filter(CursosModel.id == id & CursosModel.status == True).first()
        return result
    
    def get_cursos_by_nombre(self, nombre:str):
        result = self.db.query(CursosModel).filter(CursosModel.nombre == nombre).first()
        return result
    
    def create_cursos(self, cursos:Cursos):
        new_cursos = CursosModel(
            id= cursos.id,
            nombre= cursos.nombre,
            descripcion= cursos.descripcion,
            lineas_de_trabajo= cursos.lineas_de_trabajo,
            objetivos_especificos= cursos.objetivos_especificos,
            tipo_de_curso= cursos.tipo_de_curso
        )
        self.db.add(new_cursos)
        self.db.commit()
        return
    
    def update_cursos(self,id:int, data:Cursos):
        cursos = self.db.query(CursosModel).filter(CursosModel.id == id).first()
        cursos.nombre = data.nombre
        cursos.descripcion = data.descripcion
        cursos.lineas_de_trabajo = data.lineas_de_trabajo
        cursos.objetivos_especificos = data.objetivos_especificos
        cursos.tipo_de_curso = data.tipo_de_curso
        self.db.commit()
        return
    
    def update_status_curso(self, id:int):
        cursos = self.db.query(CursosModel).filter(CursosModel.id == id).first()
        cursos.status = False
        self.db.commit()
        return
    
    def delete_cursos(self, id:int, data:Cursos):
        self.db.delete(data)
        self.db.commit()
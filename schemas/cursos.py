from typing import Optional
from pydantic import BaseModel, Field

class Cursos(BaseModel):
    id = Optional[int] =None
    nombre: str = Field(max_length=50,min_length=5)
    descripcion: str = Field(max_length=500,min_length=10)
    lineas_de_trabajo: str = Field(max_length=500,min_length=5)
    objetivos_especificos: str = Field(max_length=500,min_length=15)
    tipo_de_curso: str = Field(max_length=500,min_length=5)

    class Config:
        schema_extra = {
            "example":{
                 "nombre": "Diplomado en seguridad social",
                 "descripcion": "Este diplomado permitira conocer y aplicar los preceptos normativos con una metodologia sencilla y pedagógica ",
                 "lineas_de_trabajo": "Se aborda el marco juridico y las politicas publicas que rigen el sistema de seguridad social en un pais determinado",
                 "objetivos_especificos":"proporcionar una información especializada en el ambito de seguridad social",
                 "tipo_de_curso":"Academico" 
            }
        }
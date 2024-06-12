from pydantic import BaseModel

class Curso(BaseModel):
    nome: str
    periodo: int
    professor: str
    horas: int
    codigo: str
    vagas:int
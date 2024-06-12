from fastapi import APIRouter, Depends
from schemas.cursos import Curso
from models.database  import get_db
from models.cursos    import Cursos
from sqlalchemy.orm   import Session

router = APIRouter()

@router.get("/cursos")
async def root():
    return {"mensagem": "Dentro de cursos"}

@router.post("/cursos")
async def criar_curso(curso: Curso, db: Session = Depends(get_db)):
    novo_curso = Cursos(**curso.model_dump())
    db.add(novo_curso)
    db.commit()
    db.refresh(novo_curso)
    return { "mensagem": "Aluno criado com sucesso",
             "aluno": novo_curso 
    }

from fastapi import APIRouter, Depends
from schemas.alunos import Aluno
from models.database  import get_db
from models.alunos    import Alunos
from sqlalchemy.orm   import Session

router = APIRouter()

@router.get("/alunos")
async def root():
    return {"mensagem": "Dentro de alunos"}

@router.post("/alunos")
async def criar_aluno(aluno: Aluno, db: Session = Depends(get_db)):
    novo_aluno = Alunos(**aluno.model_dump())
    db.add(novo_aluno)
    db.commit()
    db.refresh(novo_aluno)
    return { "mensagem": "Aluno criado com sucesso",
             "aluno": novo_aluno 
    }

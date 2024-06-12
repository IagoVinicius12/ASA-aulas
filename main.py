from fastapi import FastAPI
from typing import Optional
from routes.alunos import router as router_alunos
from routes.cursos import router as router_cursos
from models.database import engine
from models.alunos import Alunos
from models.cursos import Cursos
from models.alunos import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router_alunos)
app.include_router(router_cursos)
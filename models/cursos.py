from sqlalchemy import String, Integer, Column, TIMESTAMP, text, ForeignKey
from .database import Base

class Cursos(Base):
    __tablename__ = 'cursos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    periodo = Column(Integer, server_default="0")
    professor = Column(String(50))
    horas= Column(Integer, server_default="0")
    codigo = Column(String(40))
    vagas= Column(Integer, server_default="0")
    added_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('Now()'))
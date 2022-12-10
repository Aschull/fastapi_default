from sqlalchemy import Column, Integer, String
from app.config.db.config_db import Base
from sqlalchemy.orm import Session


class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=False, index=False)
    ano = Column(Integer, unique=False)
    
    class Config:
        orm_mode = True

    def create_aluno(self, db: Session):
        db.add(self)
        db.commit()
        db.refresh(self)
        return self
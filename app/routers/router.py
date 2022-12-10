from fastapi import APIRouter, Depends
from app.schemas.schemas import Aluno as aluno_schema
from app.models.model import Aluno as aluno_model
from app.config.db.dependencies import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/")
def health():
    return {'api': 'true'}

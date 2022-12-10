from typing import List, Optional
from pydantic import BaseModel


class Aluno(BaseModel):
    nome: Optional[str]
    ano: Optional[int]

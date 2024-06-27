# models.py

from pydantic import BaseModel

class Memo(BaseModel):
    id: int
    title: str
    content: str

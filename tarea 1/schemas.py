from pydantic import BaseModel
from pydantic.errors import DateError
from typing import Optional

class New(BaseModel):
    id: Optional[int]
    title: str
    date: str
    url: str
    media_outlet: str

class Category(BaseModel):
    value: str
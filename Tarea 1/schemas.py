from typing import List, Optional
from datetime import datetime, date


from pydantic import BaseModel


class News(BaseModel):
    id: int
    tittle: str
    date: date 
    url: str
    media_outlet: str 
    category: str
    

    class Config:
        orm_mode = True


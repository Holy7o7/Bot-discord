from fastapi import FastAPI
from fastapi.param_functions import Depends
from pydantic.utils import import_string
from db import SessionLocal
import models
import schemas
import crud
from typing import List, Union, Optional, Dict
from sqlalchemy.orm import Session
import create_db

app = FastAPI()

def get_db():
   db = SessionLocal()
   try:
      yield db
   finally:
      db.close()

@app.get("/news", response_model = List[Union[schemas.New, schemas.Category]])
def read_news(categoria: str, start: str, end: str, skip: int=0, limit: int=100, db:Session = Depends(get_db)):
   news = crud.get_news(db, categoria = categoria, start = start, end = end, skip = skip, limit = limit)
   return(news)
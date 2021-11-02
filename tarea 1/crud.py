from sqlalchemy.orm import Session
import models, schemas



def get_news(db:Session, categoria: str, start: str, end: str, skip: int=0, limit: int=100):
	return db.query(models.News).join(models.Category, models.News.id_news == models.Category.id_news).filter(models.Category.value.contains(categoria)).filter(models.News.date.between(start,end)).offset(skip).limit(limit).all()
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import true
from db import Base

class New(Base): 

    __tablename__ = "news"

    id = Column(Integer, primary_key = True)
    title = Column(String(255))
    date = Column(String(255)) 
    url = Column(String(255))  
    media_outlet = Column(String(255))

    Categories = relationship("Category", back_populates="news")

class Category(Base):

    __tablename__ = "has_category"
    
    value = Column(String(255), primary_key= true)
    id = Column(Integer, ForeignKey("news.id"))

    news = relationship("New", back_populates="Categories")
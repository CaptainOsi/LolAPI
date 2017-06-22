# -*- coding: UTF-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import desc

Base = declarative_base()

class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    url = Column(String(300))
    imgUrl = Column(String(300))
    title = Column(String(250))

    def __init__(self, url, imgUrl, title):
        self.url = url
        self.imgUrl = imgUrl
        self.title = title

    def __repr__(self):
        return "<news(%s, %s, %s)>" % (self.url, self.imgUrl, self.title)

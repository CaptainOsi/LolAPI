# -*- coding: UTF-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Promos(Base):
    __tablename__ = 'promo'

    id = Column(Integer, primary_key=True)
    url = Column(String(1000))
    image = Column(String(1000))
    item = Column(String(200))
    startdate = Column(String(20))
    enddate = Column(String(20))
    oldrp = Column(String(50))
    newrp = Column(String(50))

    def __init__(self, url, image, item, startdate, enddate, oldrp, newrp):
        self.url = url
        self.image = image
        self.item = item
        self.startdate = startdate
        self.enddate = enddate
        self.oldrp = oldrp
        self.newrp = newrp

    def __repr__(self):
        return "<news(%s, %s, %s, %s, %s, %s, %s)>" % (self.url, self.image, self.item, self.startdate, self.enddate, self.oldrp, self.newrp)

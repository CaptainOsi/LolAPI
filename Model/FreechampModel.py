from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()

class FreeChamp(Base):
        __tablename__ = 'freechamp'

        id = Column(Integer, primary_key=True)
        url = Column(String(255))
        item = Column(String(50))
        date = Column(String(20))

        def __init__(self, url, item, date):
                self.url 	= url
                self.item 	= item
                self.date 	= date

        def __repr__(self):
                return "<freechamp(%s, %s, %s)>" % (self.url, self.item, self.date)

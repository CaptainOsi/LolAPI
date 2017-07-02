# -*- coding: UTF-8 -*-
from sqlalchemy import desc

from App.connexion import *
from Model.NewsModel import News
from dictalchemy import make_class_dictable
make_class_dictable(News)

def tableautoDict(objet):
    liste = []
    for item in objet:
        liste.append(item)
    return liste

def GetArgument(objet,*args):
    dict = {}
    maliste = []
    i = 0
    while i < len(objet):
        dict = {}
        for arg in args:
            dict[arg] = str(getattr(objet[i], arg))
        maliste.append(dict)
        i = i + 1
    return maliste

def getNewsByID(id):
    news = session.query(News).filter_by(id=id).first()
    if news == None:
        return {'error: the given id is incorrect'}
    return news.asdict()


def getLastNews():
    return session.query(News).order_by(desc(News.id))[0:8]


def getNews(page, limit):
    (page, limit) = searchByPage(page, limit)
    return session.query(News).order_by(desc(News.id))[page:limit]


def getNewsSearch(search, page, limit):
    (page, limit) = searchByPage(page, limit)
    return session.query(News).filter(News.title.like('%' + search + '%')).order_by(desc(News.id))[page:limit]
    

def searchByPage(page, limit):
    if page == None:
        page = 1
    if limit == None:
        limit = 100
    page = int(limit) * (int(page) - 1)
    limit = limit + page
    if page < 0:
        page = 0
    return page, limit
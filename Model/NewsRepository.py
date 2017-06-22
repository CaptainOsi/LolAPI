# -*- coding: UTF-8 -*-
from sqlalchemy import desc

from App.connexion import *
from Model.NewsModel import News

def getNewsByID(id):
    return session.query(News).filter_by(id=id).first()

def getLastNews():
    return session.query(News).order_by(desc(News.id))[0:8]


def getNews(page=1, limit=100):
    (page, limit) = searchByPage(page, limit)

    print session.query(News).order_by(desc(News.id))[page:limit]


def getNewsSearch(search, page=1, limit=100):
    (page, limit) = searchByPage(page, limit)

    return session.query.filter(News.title.like('%' + search + '%')).order_by(desc(News.id))[page:limit]


def searchByPage(page, limit):
    page = int(limit) * (int(page) - 1)
    limit = limit + page
    if page < 0:
        page = 0

    return page, limit

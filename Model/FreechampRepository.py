# -*- coding: UTF-8 -*-
from sqlalchemy import desc

from App.connexion import *
from Model.FreechampModel import FreeChamp
from dictalchemy import make_class_dictable
make_class_dictable(FreeChamp)

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

def getFreeChampByID(id):
    return session.query(FreeChamp).filter_by(id=id).first().asdict()

def getFreeChampActual():
    t = text("SELECT * FROM freechamp where date BETWEEN adddate(now(),-7) AND now()")
    return session.execute(t)

def getFreeChamp(page, limit):
    (page, limit) = searchByPage(page, limit)
    return session.query(FreeChamp).order_by(desc(FreeChamp.id))[page:limit]

def getFreeChampLast():
    t = text("SELECT id,url,item, MAX(DATE) AS maxdate FROM freechamp GROUP BY item ORDER BY maxdate LIMIT 10")
    return session.execute(t)

def getFreeChampDate(date):
    t = text("SELECT * FROM freechamp where date BETWEEN adddate('" + date + "',-6) AND '" + date + "'")
    return session.execute(t)

def getFreeChampSearch(search, page, limit):
    (page, limit) = searchByPage(page, limit)
    return session.query(FreeChamp).filter(FreeChamp.item.like('%' + search + '%')).order_by(desc(FreeChamp.id))[page:limit]
    

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
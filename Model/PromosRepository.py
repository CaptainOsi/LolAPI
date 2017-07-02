# -*- coding: UTF-8 -*-
from sqlalchemy import desc

from App.connexion import *
from Model.PromosModel import Promos
from dictalchemy import make_class_dictable
from sqlalchemy import and_
from unidecode import unidecode
make_class_dictable(Promos)

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
            if arg == 'item':
                dict[arg] = unidecode(str(getattr(objet[i], arg)).encode('ascii','ignore'))
            else:
                dict[arg] = str(getattr(objet[i], arg))
            
        maliste.append(dict)
        i = i + 1
    return maliste

def getPromosByID(id):
    sales = session.query(Promos).filter_by(id=id).first()
    if sales == None:
        return {'error: the given id is incorrect'}
    return sales.asdict()

def getPromosActual():
    t = text("SELECT * FROM promo WHERE CURDATE( ) BETWEEN startdate AND enddate")
    return session.execute(t)

def getPromos(page, limit):
    (page, limit) = searchByPage(page, limit)
    return session.query(Promos).order_by(desc(Promos.id))[page:limit]


def getPromosSearch(search, page=1, limit=100):
    (page, limit) = searchByPage(page, limit)
    return session.query(Promos).filter(Promos.item.like('%' + search + '%')).order_by(desc(Promos.id))[page:limit]
    

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
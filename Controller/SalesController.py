# -*- coding: UTF-8 -*-
from Model.PromosRepository import *
from app import app
import json
from flask import jsonify
import urlparse
from flask_restful import Resource, Api, reqparse


@app.route('/sales', methods=['GET'])
def get_taskpromos():
    parser = reqparse.RequestParser()
    parser.add_argument('limit', type=int, help='Rate cannot be converted')
    parser.add_argument('page', type=int, help='Rate cannot be converted')
    parser.add_argument('search')
    args = parser.parse_args()
    mylimit = args['limit']
    number = args['page']
    search = args['search']
    if search == None:
        sales = getPromos(number, mylimit)
    else:
        sales = getPromosSearch(search, number, mylimit)
    sales = GetArgument(sales, 'id', 'url', 'image', 'item', 'startdate', 'enddate', 'oldrp', 'newrp')
    return jsonify(sales)


@app.route('/sales/<id>')
def getsalesbyID(id):
    sales = getPromosByID(id)
    return jsonify(sales)


@app.route('/sales/actual')
def getactualsales():
    sales = getPromosActual()
    resultList = {}
    reqList = []
    url = ""
    endate = ""
    startdate = ""
    if sales <> "":
        for row in sales:
            url = str(row['url'])
            endate = str(row['enddate'])
            startdate = str(row['startdate'])
            resultList = {'ID': str(row['id']), 'Item': str(row['item']), 'Image': str(row['image']),
                  'Price': str(row['oldrp']), 'Sale': str(row['newrp'])}
            reqList.append(resultList)
            resultList = {}
    if reqList == []:
        return jsonify({'Error: No current sales'})
    return jsonify({'Url': url, 'Date_end': endate, 'Date_start': startdate}, reqList)

# -*- coding: UTF-8 -*-
from Model.FreechampRepository import *
from app import app
import json
from flask import jsonify
import urlparse
from flask_restful import Resource, Api, reqparse

@app.route('/freechamp')
def getfreechamp():
	parser = reqparse.RequestParser()
	parser.add_argument('limit', type=int, help='Rate cannot be converted')
	parser.add_argument('page', type=int, help='Rate cannot be converted')
	parser.add_argument('search')
	args = parser.parse_args()
	mylimit = args['limit']
	number = args['page']
	search = args['search']
	if search == None:
		freechamp = getFreeChamp(number,mylimit)
	else:
		freechamp = getFreeChampSearch(search,number,mylimit)
	freechamp = GetArgument(freechamp,'url','item','date')
	return jsonify(freechamp)

@app.route('/freechamp/actual')
def getactualfreechamp():
	freechamp = getFreeChampActual()
	resultList = {}
	reqList = []
	for row in freechamp:
		resultList = {'Item': str(row['item'])}
		reqList.append(resultList)
		resultList = {}
	return jsonify({'Url': row['url'],'Date_start': row['date']}, reqList)

@app.route('/freechamp/last', methods=['GET'])
def get_tasklastfreechamp():
	sales = getFreeChampLast()
	resultList = {}
	reqList = []
	for row in sales:
		resultList = {'Url': row['url'],'Last_date': row['maxdate'],'Item': row['item']}
		reqList.append(resultList)
		resultList = {}
	return jsonify(reqList)

@app.route('/freechamp/<date>')
def getfreechampbyDate(date):
	freechamp = getFreeChampDate(date)
	resultList = {}
	reqList = []
	for row in freechamp:
		resultList = {'Url': row['url'],'Last_date': row['date'],'Item': row['item']}
		reqList.append(resultList)
		resultList = {}
	return jsonify(reqList)

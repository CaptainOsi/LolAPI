# -*- coding: UTF-8 -*-
from Model.NewsRepository import *
from app import app
import json
from flask import jsonify
import urlparse
from flask_restful import Resource, Api, reqparse

@app.route('/news/last')
def lastnews():
	news = getLastNews()
	news = GetArgument(news,'id','url','imgUrl','title')
	return jsonify(news)

@app.route('/news')
def getnews():
	parser = reqparse.RequestParser()
	parser.add_argument('limit', type=int, help='Rate cannot be converted')
	parser.add_argument('page', type=int, help='Rate cannot be converted')
	parser.add_argument('search')
	args = parser.parse_args()
	mylimit = args['limit']
	number = args['page']
	search = args['search']
	if search == None:
		news = getNews(number,mylimit)
	else:
		news = getNewsSearch(search,number,mylimit)
	news = GetArgument(news,'id','url','imgUrl','title')
	return jsonify(news)

@app.route('/news/<id>')
def getnewsbyID(id):
	news = getNewsByID(id)
	return jsonify(news)



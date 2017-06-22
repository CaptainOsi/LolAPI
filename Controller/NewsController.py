# -*- coding: UTF-8 -*-
from flask import Flask, jsonify, Response, render_template
from Model.NewsRepository import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

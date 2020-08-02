#!/usr/bin/python3
# author:zxing
# -*- coding:utf-8 -*-
# @time     : 11:31 上午
# @site     :
# @File     :app.py
# @software :PyCharm
from flask import *
import os

app = Flask(__name__)
key = os.urandom(24)
app.secret_key = key

@app.route('/')
def index():
    pass



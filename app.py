#!/usr/bin/python3
# author:zxing
# -*- coding:utf-8 -*-
# @time     : 11:31 上午
# @site     :
# @File     :app.py
# @software :PyCharm
from flask import *
import re
import os

app = Flask(__name__)
key = os.urandom(24)
app.secret_key = key


@app.route('/')
def index():
    if 'username' in session:
        flash('You were successfully logged in')
        return render_template('index.html')
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method.upper() == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            # flash('You were successfully logged in')
            session['username'] = request.form['username']
            session['password'] = request.form['password']
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(port=9527, host='0.0.0.0', debug=True)
#!/usr/bin/python3
# author:zxing
# -*- coding:utf-8 -*-
# @time     : 11:31 上午
# @site     :
# @File     :app.py
# @software :PyCharm
from flask import *
import pymysql
import os

app = Flask(__name__)
key = os.urandom(24)
app.secret_key = key


class mysql:
    def __init__(self):
        self.conn = pymysql.connect(host='120.24.148.131', user='root', passwd='zxssjdy111899', db='admin1', charset='utf8')


@app.route('/')
def index():
    if 'username' in session and 'password' in session:
        app.logger.debug(session)
        username = session['username']
        return render_template('index.html', username=username)
    return redirect(url_for('login'))


@app.route('/login/', methods=['POST', 'GET'])
def login():
    error = None
    if 'username' in session and 'password' in session:
        return redirect(url_for('index'))
    if request.method == 'POST':

        if request.form['username'] and request.form['password']:
            username, password = request.form['username'], request.form['password']
            conn = mysql().conn
            cursor = conn.cursor()
            sql = "select * from users where name='{}' and password='{}'".format(username, password)
            app.logger.debug(sql)
            cursor.execute(sql)
            n = len(cursor.fetchall())
            if n != 0:
                error = 'Login successfully'
                session['username'] = username
                session['password'] = password
                return redirect(url_for('index'))
            else:
                error = 'Login failed,check your request'
                app.logger.error(error)
                return render_template('login.html', error=error)
    return render_template('login.html')


@app.route('/logout/')
def logout():
    session.pop('username')
    session.pop('password')
    return redirect(url_for('index'))


@app.route('/register/', methods=['POST', 'GET'])
def register():
    if request.method.upper() == 'POST':
        if request.form['username'] and request.form['password'] and request.form['email']:
            username, password, email = request.form['username'], request.form['password'], request.form['email']
            conn = mysql().conn
            cursor = conn.cursor()
            sql = "insert into users (name, password, email) values ('{}','{}','{}')".format(username, password, email)
            app.logger.debug(sql)
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()

            return redirect(url_for('login'))
        else:
            error = 'Register failed,please check your request'
            return render_template('register.html', error=error)

    return render_template('register.html')


if __name__ == '__main__':
    app.run(port=8080, debug=True)
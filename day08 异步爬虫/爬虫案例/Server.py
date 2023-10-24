#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask,render_template
from time import sleep
#安装flask模块

#1.实例化app对象
app = Flask(__name__)

@app.route('/main')
def main():
    return 'i am main'
@app.route('/bobo')
def index1():
    sleep(2)
    return render_template('test.html')
@app.route('/jay')
def index2():
    sleep(2)
    return render_template('test.html')
@app.route('/tom')
def index3():
    sleep(2)
    return render_template('test.html')

if __name__ == "__main__":
    app.run()
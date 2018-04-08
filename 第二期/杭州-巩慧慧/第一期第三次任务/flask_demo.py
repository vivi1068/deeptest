#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-4-3 下午11:13
# @Author  : gonghuihui
# @File    : flask_demo.py
# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/api')
# def index():
#     return "Hello World!"
#
# if __name__ == "__main__":
#     app.run()

from flask import Flask
from flask import jsonify
from flask import request,Response
import random
import time

app = Flask(__name__)

# 生成随机字符串
def random_str():

    data = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+"

    random.seed(time.time())

    sa = []
    for i in range(8):
        sa.append(random.choice(data))
    salt = ''.json(sa)

    return salt

def make_respnse():
    content = '{"result": "%s", "data": "%s"}' % (random_str(), random_str())
    resp = Response(content)
    resp.headers["Access-Control-Origin"] = '*'
    return resp

# http GET
@app.route("/query", methods=["GET"])
def query():
    return jsonify(
        username = random_str(),
        password = random_str()
    )

@app.route("/update", methods=["POST"])
def update():
    return make_respnse()

@app.route("/delete", methods=["DELETE"])
def delete():

    return make_respnse()

@app.route("/head", methods=["HEAD"])
def head():
    return make_respnse()

if __name__ == "__main__":
    app.run(debug=True)
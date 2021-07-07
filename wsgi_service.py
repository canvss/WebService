# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/7/7 21:48
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
from wsgiref.simple_server import make_server
from utils.read_data_utils import *


def login(environ):
    return read_data('html/login.html')

def index(environ):
    return read_data('html/index.html')

def favicon(environ):
    return read_data('images/favicon.ico')


def application(environ,start_response):
    # 获取请求path
    pathinfo = environ.get('PATH_INFO')
    # 返回响应头设置
    start_response("200 OK", [('Content-Type', 'text/html; charset=utf-8')])
    # if pathinfo == '/favicon.ico':
    #     return [read_data(path='images/favicon.ico')]
    # elif pathinfo == '/login':
    #     data = read_data(path='html/login.html')
    # elif pathinfo == '/index':
    #     data = read_data(path='html/index.html')
    # else:
    #     data = read_data(path='html/404notFound.html')
    # return [data.encode('utf8')]

    url_patterns=[
        ('/login',login),
        ('/index',index),
        ('/favicon.ico',favicon)
    ]

    func = None
    for item in url_patterns:
        if pathinfo == item[0]:
            func = item[1]
            break

    if func:
        return [func(environ)]
    else:
        print('this is 404 not found!!')
        return [read_data('html/404notFound.html')]
httped = make_server('127.0.0.1',8881,application)
# 开始监听http请求
httped.serve_forever()

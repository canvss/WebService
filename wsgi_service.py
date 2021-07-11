# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/7/7 21:48
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
from wsgiref.simple_server import make_server
from urls import *



def application(environ,start_response):
    # 获取请求path
    pathinfo = environ.get('PATH_INFO')
    # 返回响应头设置
    start_response("200 OK", [('Content-Type', 'text/html; charset=utf-8')])

    func = None
    for item in url_patterns:
        if pathinfo == item[0]:
            func = item[1]
            break

    if func:
        return [func(environ)]
    else:
        return [read_data('html/404notFound.html')]

addr = '127.0.0.1'
port = 8086
httped = make_server(addr,port,application)
print('web服务器启动成功！%s:%s'%(addr,port))
# 开始监听http请求
httped.serve_forever()

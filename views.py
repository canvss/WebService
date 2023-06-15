# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/7/8 21:11
# @Author   :canvs
# @Email    :canvs@qq.com
------------------------------
"""
from utils.read_data_utils import *

def login(environ):
    if environ.get('REQUEST_METHOD') == 'POST':
        pass
    elif environ.get('REQUEST_METHOD') == 'GET':
        return read_data('html/login.html')
def index(environ):
    print(environ)
def favicon(environ):
    return read_data('images/favicon.ico')

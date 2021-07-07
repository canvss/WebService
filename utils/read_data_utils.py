# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/7/7 21:58
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""

def read_data(path):
    with open(path,'rb') as f:
       data = f.read()
    return data

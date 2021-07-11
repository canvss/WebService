# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/7/11 22:13
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
import socket
from datetime import datetime

server = socket.socket()
addr = '127.0.0.1'
port = 8086
server.bind((addr,port))
server.listen(5)
print('web服务器启动成功！%s:%s'%(addr,port))
while True:
    # 获取conn，addr
    conn, addr = server.accept()
    # 获取浏览器传来的数据
    data = conn.recv(1024)
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('html/index.html','r') as f:
        data = f.read().replace('{{time}}',str(time))

    response = 'HTTP/1.1 200 ok \r\n\r\n %s' % data
    conn.send(response.encode('utf-8'))
    conn.close()


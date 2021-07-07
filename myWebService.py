import json
import socket

socket = socket.socket()
socket.bind(('127.0.0.1', 8880))
socket.listen(5)

while True:
    print('service waiting.......')
    conn, addr = socket.accept()
    data = conn.recv(1024)

    data = json.loads(data)

# 读取html文件
with open("html/login.html", "rb") as f:
    data = f.read()
conn.send((b'HTTP/1.1 200 ok\r\n\r\n%s' % data))
conn.close()

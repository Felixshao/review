import socket
import sys


def server_one():
    """服务端"""
    # 创建socket对象
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 获取主机名
    host = socket.gethostname()
    print(host)
    port = 9999
    # 绑定端口号
    serversocket.bind((host, port))
    # 设置最大连接数
    serversocket.listen(5)

    # 建立客户端连接
    while True:
        clientsocket, addr = serversocket.accept()      # accept()等待客户端连接
        print('连接地址: {}'.format(addr))
        msg = '欢迎访问felix服务端!'
        clientsocket.send(msg.encode('utf-8'))  # 返回服务的数据
        clientsocket.close()    # 关闭套接字


if __name__ == '__main__':
    server_one()




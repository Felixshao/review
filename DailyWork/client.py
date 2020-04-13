import socket
import sys


def client_tow():
    """客户端"""
    # 创建stock对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 获取主机名
    # host = socket.gethostname()
    host = 'DESKTOP-8RDF0EE'
    # 设置端口
    port = 9999
    # 连接服务端
    s.connect((host, port))
    # 接收服务端小于1024字节的数据
    msg = s.recv(1024)
    # 关闭客户端
    s.close()
    # 输出服务端返回信息
    print(msg.decode('utf-8'))


if __name__ == '__main__':
    client_tow()
import hashlib
from flask import Flask, request
import json

name = 'xiao'
pwd = '123456'
server = Flask(__name__)


@server.route('/login', methods=['get', 'post'])
def login():
    username = request.values.get('name')
    password = request.values.get('pwd')

    h1 = hashlib.md5()  # 创建加密对象
    h2 = hashlib.md5()  # 创建加密对象

    h1.update(name.encode(encoding='utf-8'))    #
    h2.update(pwd.encode(encoding='utf-8'))

    name_md5 = h1.hexdigest()
    pwd_md5 = h2.hexdigest()

    if username and password:
        if username == name_md5 and password == pwd_md5:
            resu = {'code': 200, 'msg': 'pass'}
            return json.dumps(resu, ensure_ascii=False)
        elif username != name_md5:
            resu = {'code': 201, 'msg': 'name error!'}
            return json.dumps(resu, ensure_ascii=False)
        elif password != pwd_md5:
            resu = {'code': 201, 'msg': 'pwd error!'}
            return json.dumps(resu, ensure_ascii=False)
    else:
        resu = {'code': 202, 'msg': '参数不能为空!'}
        return json.dumps(resu, ensure_ascii=False)


if __name__ == '__main__':

    server.run(debug=True, port=8882, host='127.0.0.1')

    # h1 = hashlib.md5()  # 创建加密对象
    # h2 = hashlib.md5()  # 创建加密对象
    #
    # name = 'xiao'
    # pwd = '123456'
    # h1.update(name.encode(encoding='utf-8'))
    # h2.update(pwd.encode(encoding='utf-8'))
    # name_md5 = h1.hexdigest()
    # pwd_md5 = h2.hexdigest()
    # print(name_md5, pwd_md5)

    # d2bf7126723ea8f6005ba141ea3c3e2c e10adc3949ba59abbe56e057f20f883e

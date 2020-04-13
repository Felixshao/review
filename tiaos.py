import hashlib
import requests


def md5_parameter_get():
    url = 'http://127.0.0.1:8882/login'
    parame = {'name': 'xiao', 'pwd': '123456'}
    for i in parame:
        h1 = hashlib.md5()
        h1.update(parame[i].encode(encoding='utf-8'))
        parame[i] = h1.hexdigest()
    login = requests.get(url, params=parame, verify=False)
    print(login.text)

def md5_parameter(name):
    parame = {'name': name, 'pwd': '123456'}
    for i in parame:
        h1 = hashlib.md5()
        h1.update(parame[i].encode(encoding='utf-8'))
        parame[i] = h1.hexdigest()
    print(parame['name'])
    return parame['name']


if __name__ == '__main__':
   md5_parameter('xiao')


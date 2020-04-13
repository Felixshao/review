import paramiko

def remotConnect():
    """远程连接Linux"""
    # 服务器信息
    host = '192.168.1.107'
    user = 'test'
    password = '13691916244shaos'

    # 创建SSHclient对象
    ssh = paramiko.SSHClient()
    # 通过公共方式认证（不需要在known_hosts 文件中存在)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接远程机器
    ssh.connect(host, username=user, password=password, timeout=10)
    # 输入linux命令
    ip = 'ifconfig'
    stdin, stdout, stderr = ssh.exec_command(ip)
    # 输出命令执行结果
    result = stdout.read()
    print(stdin, '\n', stderr, '\n', stdout)
    print(result.decode('utf-8'))
    # 关闭连接
    ssh.close()


if __name__ == '__main__':

    remotConnect()
# _*_ config: utf-8 _*_
# 面试题   https://blog.csdn.net/qq_34671951/article/details/88683456?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase

# 迭代器test
def diedaiqi_test():
    def add(n, i):
        return n + i

    # 生成器
    def test():
        print('test')
        for i in range(4):
            yield i

    t = test()  # 迭代器

    for n in [1, 10, 5]:
        # 迭代器对象取完值后再取值报错或为空
        # t为迭代器对象，迭代器取值时值不变化
        # 迭代器对象调用时带公式过去
        # 迭代逻辑：
        # n = 1时: t = (add(1, i) for i in t)    # t值不变，为[0, 1, 2, 3]
        # n = 10时: t = (add(1, i) for i in (add(1, i) for i in t))   # t值不变，为[0, 1, 2, 3]
        # n = 5时: t = (add(1, i) for i in ((add(1, i) for i in (add(1, i) for i in t))))     # t值不变，为[0, 1, 2, 3]
        t = (add(n, i) for i in t)

    print(list(t))  # 结果[15, 16, 17, 18]

# super面试题
# super方法，用于调用父类(超类)的一个方法。
# python3中用法：在继承类中使用super方法直接可以调用父类函数   # super().test1(num, num2)
# python2中用法: 在继承类中使用super方法需传入继承类名和self，才能调用父类函数   # super(sonClass, self).test1(num, num2)
class baseClass:
        def test1(self, num, num2):
            print(num + num2)

class sonClass(baseClass):
        def test2(self):
            super().test1(num, num2)
son = sonClass()
son.test1(15, 20)


# 三：L = [1, 2, 3, 11, 2, 5, 3, 2, 5, 3]，用一行代码得出 [11, 1, 2, 3, 5]。
def list_quchong():
    L = [1, 2, 3, 11, 2, 5, 3, 2, 5, 3]
    print(list(set(L)))     # 将list先转换成集合即可去重，集合是无序的


# 四：L = [1, 2, 3, 4, 5]，L[10:]的结果是？
def list_qiepian():
    L = [1, 2, 3, 4, 5]
    print(L[10:])   # 结果：空列表，原因：列表切片允许超出索引


# 五：L = [1, 2, 3, 5, 6]，如何得出 '12356'？
def list_str():
    L = [1, 2, 3, 5, 6]
    L2 = ['1', '2', '3', '5', '6']

    n2 = ''.join(L2)    # list中值为str可以使用join方法
    print(n2, type(n2))

    n = ''
    for i in L:     # list中值为int，只能循环组合
        n = n + str(i)
    print(n, type(n))


# 六、列表和字典有什么区别？
# 字典格式为键对值方式
# （1）获取元素的方式不同。列表通过索引值获取，字典通过键获取。
# （2）数据结构和算法不同。字典是hash算法，搜索的速度特别快。
# （3）占用的内存不同。

# 七、如何结束一个进程？
# 1.terminate()方法
# 2.subprocess.Popen()方法
def kill_process():
    import subprocess
    windows_kill_yingyong = 'taskkill /f /t /im chromedriver.exe'    # 强制杀死此应用进程
    windows_kill_process = 'taskkill /f /t /im 18911'   # 杀死此进程，通过命令可查看应用进程：tasklist | findstr 应用名称
    subprocess.call(windows_kill_yingyong)


# 八、进程、线程有什么区别？什么情况下用进程？什么情况下用线程？
#   (1): 进程之间相互独立，线程之间数据共享

# 九：10、什么是ORM？为什么要用ORM？不用ORM会带来什么影响？
# 答：
# ORM框架可以将类和数据表进行对应，只需要通过类和对象就可以对数据表进行操作。
# 通过类和对象操作对应的数据表，类的静态属性名和数据表的字段名一一对应，不需要写 SQL 语句。
# ORM另外一个作用，是根据设计的类生成数据库中的表。

# 十、写一段代码，ping 一个 ip地址，并返回成功、失败的信息。
def python_ping_ip():
    import os, subprocess
    cmd = 'ping 192.168.31.199'
    result = os.popen(cmd)
    print(result.read())    # 读取返回信息

    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE)  # 运行adb命令，并保存输入内容
    print(popen.stdout.read().decode('utf-8'))  # 获取adb命令运行结果, 并设置编码
    popen.kill()  # 结束后杀死子进程


# 十一、说说接口测试的流程，介绍一下 request 有哪些内容。
# 流程：获取接口文档，依据文档设计接口参数，获取响应，解析响应，校验结果，判断测试是否通过。
# request内容：
# 1.封装各种请求：get/post
# 2.以关键字参数形式封装了关键字: params/data/json/headers/token
# 3.封装响应内容：json/status_code/cookies/url
# 4.session请求，可以跨请求
def requests_test():
    import requests, warnings, json

    warnings.filterwarnings('ignore')

    s = requests.session()
    url = 'https://api.apiopen.top/getTangPoetry?page=1&count=20'
    news = s.get(url, params='', headers='', verify=False)
    text = news.text
    print(type(json.dumps(text)))
    print(news.status_code)
    print(news.cookies)
    print(news.url)
    print(news.headers)
    print(news.apparent_encoding)


# 十二、ui自动化，如何做集群？
# selenium grid
# 部署环境：python3+jdk+1个hub+n个node+Remode+浏览器driver
def selenium_grid():
    from selenium.webdriver import Remote

    node_list = {'http://169.254.163.156:4455/wd/hub': 'chrome'}    # 节点地址和选择的浏览器

    for host, browse in node_list.items():
        driver = Remote(command_executor=host, desired_capabilities={
            'platfomr': 'ANY',
            'browsename': browse,
            'version': '',
            'javascriptEnable': True
        })
        driver.find_element_by_id('id').click()

# 十三、移动端 UI 自动化，经常会自动安装 2 个程序，你知道那两个程序是什么东西不？
# 守护精灵（unlock和appium settings）， 注释掉两行安装命令

# 十四：说5个以上 Linux 命令。
# find -name 文件名称   # 查找命令
# ln -s 目标目录 软连接地址  # 创建软连接命令
# iostat -c # cpu状态值，如不能使用， 安装sysstat，命令：yum -y install sysstat
# chmod 777 文件  # 赋予读写执行权限，r：4， w：2，x：1
# tar -xzvf 文件  # 解压文件后缀为tar.gz     x:解压tar文件, z: gz文件解压或创建， v:显示解压/压缩过程，f:指定文件
# tar -xvf 文件  # 解压文件后缀为tar
# su 用户名   # 切换用户
# ps  -A    # 查看全部进程
# top   # 查看监控器
# vim   编辑文件
# cat   # 查看文件内容

# 十五：介绍一下你在这个项目中是如何使用 Jenkins 的。
# 1.进入jenkins，创建项目，然后配置
# 2.配置源码管理：跑本地就选无；跑git选git，传入项目的git路径和账号密码+分支
# 3.构建触发器：一般选定时和代码更新就跑：命令：分 时 日 月 星期
# 4.构建：win上选择window，linux选择shell，输入运行命令保存即可

# 十六：数据驱动
import ddt, unittest, paramunittest

data_list = [[1, 2, 3, 4], [4, 8, 9, 10]]

@ddt.ddt
class shuju(unittest.TestCase):

    @ddt.data(*data_list)
    def test_ddt(self, data):
        print('index: ', data_list.index(data))
        print('data:', data)

@paramunittest.parametrized(
    data_list
)
class shuju2(unittest.TestCase):

    def setParameters(self, num, num2):
        self.num = num
        self.num2 = num2

    def test_parameunittest(self):
        print(data_list.index(self.num), '  ', self.num)
        print(data_list.index(self.num2), '  ', self.num2)


# 十七、浮点数计算
# 判断断言是否成功， 考浮点数运算知识
def float_test():
    a = 0.1
    b = 0.2
    c = 0.3
    # assert a + b == c   # 断言失败，报AssertionError错，原因：10 进制表示方式会丢掉它的精度，看似有穷的小数实际是无穷的

    # 解决方法,使用decimal库，Decimal()方法可以保持精度，但传参需为字符，否则一样失去精度
    from decimal import Decimal
    assert Decimal(str(a)) + Decimal(str(b)) == Decimal(str(c))


# 十八：列表的扁平化和降维
# 有一个二维列表，降成普通的一维的。比如说柠檬班都会有学员分组，我们想通过分组信息去获取所有的学员名称。
#
# groups = [['huahua', 'xiaojian'], ['musen', 'yuze'], ['keyou']]
# # 得到结果 ['huahua', 'xiaojian', 'musen', 'yuze', 'keyou']
def list_jiangwei():
    groups = [['huahua', 'xiaojian'], ['musen', 'yuze'], ['keyou']]
    groups2 = [j for i in groups for j in i]    # 方法1，推导式
    groups3 = sum(groups, [])   # 方法2, sum方法
    print(groups2)
    print(groups3)

# 十九：多继承问题
# 题目1:C().test()结果为？
class A:
    def test(self):
        print('a is running')

class B:
    def test(self):
        print('b is running')

class C(A, B):
    pass

def duojic_result():
    C().test()
    print(C.__mro__)    # 查看类运行顺序
# 结果为:a is running; 按顺序继承，先走前面的


# 题目2:E(().test()结果为？
class A:
    def test(self):
        print('a is running')

class B(A):
    pass

class D(A):
    def test(self):
        print('d is running')

class E(B, D):
    pass

def duojic_result2():
    E().test()
    print(E.__mro__)    # 查看类运行顺序
# 结果为:d is running ; 按顺序继承+菱形方式，顺序:E->B->D->A


# 题目2:F(().test()结果为？
class A:
    def test(self):
        print('a is running')

class B(A):
    pass

class D:
    def test(self):
        print('d is running')

class F(B, D):
    pass

def duojic_result3():
    F().test()
    print(F.__mro__)    # 查看类运行顺序
# 结果为:d is running ; 按顺序继承+V形方式，顺序:F->B->A->D

# 二十、_ init _ _ 和 _ _ new _ _是什么？
# 代码：
class init_new(object):
    def __new__(cls, num):  # 作用: 创建实例对象，通过return方法返回；调用类就会执行，执行在init之前，且init传参需和new一致
        print("__new__方法执行了")
        return object.__new__(cls)

    def __init__(self, num):    # 一般用于初始化，调用类就会执行init
        print("__init__方法执行了")
        self.num = num
        print(self.num)

    def __del__(self):  # 调用类结束时自动调用del方法，可用于最后处理
        print("__del__方法执行了")

    def __str__(self):  # 只要print输出了类，就会调用此方法，输出return的数据
        print("__str__方法执行了")
        return 'class init_new'

    def test_pr(self):

       return 1

def init_new_test():
    t = init_new(10)
    print(t)    # 测试str方法

# 二十一: 什么是pass，什么是lambda函数？
# 答案：pass为空语句，lambda创建匿名函数
def pass_lambda():
    b = lambda a: a + a
    print(b(1))

# 二十二: is和==有什么区别？
# is：对比两个对象的地址是否一致，通过id()可查看地址
# ==: 对比两个对象的值是否一致
def isis():
    a = 'str'
    print(id(type(a)))
    print(id(str))

# 二十三: *args和**kwargs的区别？
# *args将数据打包成元组
# **kwargs将数据打包成dict，参数类型:a=1, b=1
def args_kwargs(*args, **kwargs):

    def test():

        print('*args:', args, '; **kwargs:', kwargs)
    return test()

def print_a():
    args_kwargs('1', 2, 3, a=1, b=2, c=3)


# 二十四: re模块
def re_modle():
    import re
    str = '你好-》这是一个123456'
    print(re.match('你好', str).span())    # 匹配字符是否为字符串开头，不是返回None，是的话.span()返回字符在字符串的位置

    print(re.search('这是', str).span())    # 搜索字符是否属于字符串，不是返回None，是的话.span()返回字符在字符串的位置
    p = re.compile('这是|你|12')   # 设置替换的内容
    print(p.sub('替换', str))     # 传参:被替换成的文本，需要被替换的文本，返回字符串
    print(p.subn('subn', str))  # 返回元组(替换后的字符串，替换的个数)

# 二十五: 使用sort排序，在从最后一个元素开始判断,达到去重和排序
def sort_daoone():
    a = [1,2,4,2,4,5,7,10,5,5,7,8,9,0,3]
    a.sort(reverse=True)        # 加入reverse设置为True，降序排序，去掉或false升序
    last = a[-1]
    for i in range(len(a) - 2, -1, -1):  # range(start, end, scan)开始、结束、间隔
        if a[i] == last:
            del a[i]
        else:
            last = a[i]
    print(a, last)

# 二十六：Python里面如何拷贝一个对象？（赋值，浅拷贝，深拷贝的区别）
def copy_object():
    a = 10
    b = a
    b = 15
    print(a, b, id(a), id(b))  # 1.赋值方式


# 二十七：冒泡排序
def maopao_sort():

    list_value = [1, 2, 3, 15, 20, 16, 8]
    for i in range(len(list_value) - 1):
        for j in range(0, len(list_value) - 1):
            stmp = list_value[j]
            if list_value[j] > list_value[j+1]:
                list_value[j] = list_value[j+1]
                list_value[j+1] = stmp
            print(list_value, end=' ')
        print()
    print(list_value)

# 二十八：列表与元组的区别
# 1.列表是动态数据，值可变，大小可变
# 2.元组是静态数据，值不可变，大小不可变

# 二十九: http的请求流程是怎么样的
# 1.客户端和服务端建立tcp请求（客户端请求DNS服务器，获取相应域名对应的ip，通过ip找到对应的服务器，和服务器建立tcp连接）
# 2.客户端向服务端发送requests请求
# 3.服务端向客户端回复response响应
# 4.客户端和服务端断开tcp连接

# 三十: 你怎么理解token，cookie，session
# token: 身份令牌，唯一的，对每次请求生成不同的签名，比session安全性高
# cookies：存储在浏览器中，一种身份，可保存一段时间（服务器生成发送给浏览器，存储在浏览器，下次访问发送cookies来识别机器）
# session：存储在服务器，存储身份信息，断开连接了session就销毁了；问题：负载均衡时，访问另一台服务会出现session丢失

# 三十一：怎么获取token，中间会用到那些思路
# 1.浏览器登录后，在f12的application中查看cookies，在cookies中获取token
# 2.获取请求，获取cookies，拿到token

# 三十二：接口参数关联时怎么解决，如何实现
# 方法一: 使用公共参数
num = 10
class global_guanl():

    def shengc_params(self):
        global num
        num = 15

    def shiy_params(self):

        nums = num + 10
        print(nums)

# 三十三：你怎么理解多个元素定位的方式，它的数据类型是什么
# 找到所有元素，存入list中
def elements_type():
    import time
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    driver.find_element_by_id('kw').send_keys('test')
    time.sleep(1)
    driver.find_element_by_id('su').click()
    time.sleep(2)
    text = driver.find_elements_by_class_name('t')
    print(text[0].text)
    for i in text:
        print(i.text)

# 三十四：在自动化测试中，数据如何分离
# 定位元素放置page文件中，接口放置excel表，配置文件放置ini文件

# 三十五：使用什么模式可以整合web和移动的UI测试、
# 我：封装selenium的基础方法(如：操作元素、点击、传值等)， 封装appium的基础方法并继承selenium

# 三十六：接口自动化框架设计总结
# 1.使用unittest单元测试框架设计和管理用例，使用ddt驱动用例
# 2.对requests原始请求封装
# 3.对python操作excel管理读取方法封装，调用
# 4.将接口测试案例中的测试数据分离的excel中，并优化原有代码
# 5.对接口测试用的动态参数赋值和调用
# 6.编写主程序，运行所有接口测试用例
# 7.引入logging日志文件，对接口执行过程中出现的异常情况进行跟踪、管理
# 8.引入config配置，将使用到的配置信息管理
# 9.加入BeautifulReport和ygmail来输出报告和发送邮件

# 三十七：mock搭建和使用


if __name__ == '__main__':
    elements_type()


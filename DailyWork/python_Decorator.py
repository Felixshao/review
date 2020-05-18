# _*_ config: utf-8 _*_
# python装饰器
# 理解装饰器的前提: 1.所有东西都是对象(函数可以当做对象传递) 2.闭包
import time
from functools import wraps

# 装饰器原型，传入对象为函数
def decorator_one(func):
    # 闭包， 无参数
    def decorator_one_in():
        start_t = time.time()
        func()
        end_t = time.time()
        print('spend {} secs'.format(end_t-start_t))
    return decorator_one_in

# 装饰器原型，传入对象为函数
def decorator_tow(func):
    # 闭包，有参数，加入wraps装饰器，函数使用装饰器时改变函数元信息
    @wraps(func)
    def decorator_two_in(a, b):
        start_t = time.time()
        func(a, b)
        end_t = time.time()
        print('spend {} secs'.format(end_t-start_t))
    return decorator_two_in

# 对原有装饰器再封装，返回一个装饰器(一个含有参数的闭包)
def decorator_zhu(d):
    def decorator_three(func):
        # 闭包，有参数

        def decorator_three_in(a, b):
            start_t = time.time()
            func(a, b)
            end_t = time.time()
            print('spend {} secs'.format(end_t-start_t))
            if d:
                print('此操作存入日志')
            if d == 10:
                print('d: ', d)
        return decorator_three_in
    return decorator_three


# 类装饰器,一般依靠内部方法__call__
class decorator_class_one(object):

    def __init__(self, func):
        self._func = func

    def __call__(self, a, b):
        start_t = time.time()
        self._func(a, b)
        end_t = time.time()
        print('spend {} secs'.format(end_t - start_t))

    # property装饰器，将函数变成属性, decorator_class_one().width方法获取
    @property
    def width(self):
        return self._width

    # .setter方法，给属性赋予设置权限
    @width.setter
    def width(self, width):
        if not AttributeError(width):
            raise AttributeError('width属性设置错误')
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    # .setter无设置的话，属性只有只读权限
    @property
    def resolution(self):
        return self._height * self._width

# 对象函数
def test():
    print('test...')
    time.sleep(3)

# 不带函数的装饰器
@decorator_one
def test2():
    print('test2...')
    time.sleep(2)

# 带参数的被装饰的函数
@decorator_tow
def test3(a, b):
    print('test3..., {} + {} = {}'.format(a, b, a+b))
    time.sleep(1)

# 带参数的装饰器
@decorator_zhu(10)
def test4(a, b):
    print('test4..., {} + {} = {}'.format(a, b, a + b))
    time.sleep(0.5)


# 类装饰器
@decorator_class_one
def test5(a, b):
    print('test5..., {} + {} = {}'.format(a, b, a + b))
    time.sleep(0.5)

# 解决装饰器对原函数的元信息改变方法，在装饰器闭包函数加入warps装饰器
@ decorator_tow
def test6():
    print('test6,...')


if __name__ == '__main__':
    # 装饰器缺点：
        # 1.位置错误的代码->不要在装饰器之外添加逻辑功能
        # 2.不能装饰@staticmethod 或者 @classmethod已经装饰过的方法
        # 3.装饰器会对原函数的元信息进行更改,比如函数的docstring,__name__,参数列表:
    decorator = decorator_class_one(test5)
    # decorator()
    # test2()
    # test3(1, 2)
    test4(2, 3)
    # test5(3, 4)
    # print(test2.__name__)   # 不加入wraps装饰器，函数名称显示为闭包函数名
    # print(test6.__name__)   # 不加入wraps装饰器，函数名称显示为本身的函数名
    decorator.width = 100   # 赋予属性值
    decorator.height = 20
    print(decorator.width)  # 读取属性值
    print(decorator.height)
    print(decorator.resolution)

    test5(10, 20)




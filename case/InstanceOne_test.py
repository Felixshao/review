# -*- coding: utf-8 -*-
# @Time     : 2019.4
# @Author   : felix
# @Email    : shaoyufei1234@163.com
# @File     : InstanceOne_test.py
# @Software : PyCharm


import cmath
import random
import re
import time
from numpy.core._multiarray_umath import lcm
from public import public
from math import factorial, gcd

"""1数字求和"""
def number_sum():

    while True:
        a = input('输入第一个数字a：')
        b = input('输入第二个数字b：')
        try:
            c = float(a) + float(b)        # 求和
            d = c - int(c)                 # 获取小数点后的值
            break
        except BaseException as b:
            print(b)
            print('输入的非数字，请重新输入!')
    if d == 0:      # 小数点后为0时，转换成整型输出
        print(a, '+', b, '=', int(c))
    else:
        print(a, '+', b, '=', c)


"""2.1计算平方根(只适用正数)"""
def square_Root():

    a = input('请输入数字：')
    b = float(a) ** 0.5           # 计算出平方根
    c = b - int(b)                # 获取小数点后的值
    if c == 0:
        print('%s的平方根为：%d' % (a, b))
    else:
        print('数字%s的平方根为: %f' % (a, b))


"""2.2计算平方根(适用于实数、负数和复数)"""
def square_Root2():
    a = float(input('请输入数字：'))
    b = cmath.sqrt(a)       # cmath.sqrt开平方根方法
    if a >= 0:
        print('%s的平方根为：%f' % (a, b.real))           # b.real获取数字b实数部分，b.imag获取虚数部分
    else:
        print('%f的平方根为：%f+%fj' % (a, b.real, b.imag))    # 复数在实数部分无平方根，在复数中平方根为实数加虚数


# """3计算二次方程"""
# def equation():
#     a = float(input("输入a："))
#     b = float(input("输入b："))
#     c = float(input("输入c："))
#
#     d =
#
#     print(d)


"""4计算三角形面积"""
def Triangle_area():
    a = float(input("输入第一边长："))
    b = float(input("输入第二边长："))
    c = float(input("输入第三边长："))

    p = (a + b + c) / 2         # 求三角形的半周长

    # 海伦公式（利用三角形周长求面积），半周长分别减去三边，所得数相乘，得到乘积后乘以半周长，所得数的平方根即为三角形面积
    s = (p * (p-a) * (p-b) * (p-c)) ** 0.5

    flag = isinstance(s, complex)
    if flag:
        print('三边无法构成三角形，请重新输入!')
        Triangle_area()
    else:
        print("三边长分别为%f、%f、%f的三角形的面积为：%f" % (a, b, c, s))


"""5计算圆的面积"""
def Round_area():
    PI = 3.1415
    r = input("输入圆的半径：")

    if r.isdigit():                 # 判断r是否为数字
        s = PI * float(r) ** 2
        print("半径为%f的圆的面积为：%.2f" % (float(r), s))
    else:
        print('输入的非数字，请重新输入！')
        Round_area()


"""6类型判断"""
def Type_assert():
    a = input('请输入：')

    if a.isdigit():
        print('字符为数字')
    elif a.isalpha():
        print('字符为字母')
    elif a.isalnum():
        print('是字母或数字')


"""7猜测随机数游戏"""
def get_random():
    print('猜数据数游戏，游戏规则如下：\n1.猜测0-100间的数字；\n2.输入后，没猜中会提示数字大或小了;\n3.7次猜测机会。')
    num = random.randint(0, 100)
    for i in range(8):
        if i == 7:
            print('失败，游戏结束！')
            break
        a = int(input('请输入：'))
        if a > num:
            print('大了, ', end='')
        elif a < num:
            print('小了, ', end='')
        elif a == num:
            print('恭喜你，答对了！')
            break


"""8：摄氏温度转华氏温度"""
def temperature():

    celsius = float(input("请输入摄氏温度："))       # 输入摄氏温度，并转为浮点型数据
    fahrenheit = (celsius * 1.8) + 32            # 摄氏度转华氏温度公式

    print('%0.2f 摄氏度转为华氏温度为 %0.2f' %(celsius, fahrenheit))


"""9：交换变量"""
def switch():

    x = input("请输入值x：")
    y = input("请输入值y：")

    temp = x
    x = y
    y = temp

    print("输出交换变量后的值：x = %s, y = %s" % (x, y))


    pass


"""10：if语句"""
def if_else():

    while True:
        try:
            x = float(input("请输入一个数字："))
            if x == 0:
                print("输入数字为0")
            elif x > 0:
                if x < 10:
                    print("输入数字为正数，且是一位数")
                else:
                    print("输入数字为正数，且不是一位数")
            else:
                print("输入的数字为负数")
            break
        except ValueError as v:
            print("输入无效，需要输入一个数字")


"""10：判断字符串是否为数字"""
def judge_number():
    # print(is_number('123'))
    print('判断字符串是否为数字游戏!\n输入结束程序中断运行，输入其他继续')
    while True:
        a = input('请输入数字：')
        # print(isnumeric('qwe'))
        if a == '结束':
            print('结束')
            break
        else:
            flag = public.isdigit(a)
            if flag:
                print('输入为数字，正确')
            else:
                print('输入的不是数字')
            # print(public.isdigit(a))               # 重构的判断数字方法，认定数字、小数和负数为True
            # print(a.isdigit())            # 自带的判断字符串方法，只认定正整数为True


"""11.判断奇数和偶数"""
def odd_or_even():
    print("判断数字为奇数或偶数游戏，输入结束停止运行，输入其他继续！")
    while True:
        x = input('请输入整数：')
        flag = public.isdigit_two(x)    # 判断输入的字符串为整数的方法
        if x == '结束':
            print('游戏结束')
            break
        elif flag:
            if int(x) % 2 == 0:         # 能整除2的整数为偶数
                print('%d为偶数' % (int(x)))
            else:
                # print('%d为奇数' % (int(x)))
                print('{0}为奇数'.format(int(x)))
        else:
            print('输入的不是整数')


"""12.判断是否为闰年"""
def judge_leapyear():
    print('判断是否为闰年游戏，输入结束停止运行，输入其他继续！')
    while True:
        year = input("请输入年份：")
        flag = year.isdigit()
        if year == '结束':
            print('游戏结束！')
            break
        elif flag:
            year = int(year)
            if year == 0:
                print('无此年份！')
            elif(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 3200 != 0) or (year % 172800 == 0):
                print("{0}为闰年".format(year))
            else:
                print('{0}不是闰年'.format(year))
        else:
            print('输入的不是年份!', end='')


"""13.获得最大值函数"""
def max_num():

    numTuble = (13, 45, 90, 12, 145)        # 元组
    numList = [1, 2, 54, 155, 90, 55]       # 列表
    numSet = {55, 123, 99, 109, 155, 2908}  # 集合
    print(type(numTuble), type(numList), type(numSet))
    print("{0}中最大值为{1}".format(numTuble, max(numTuble)))
    print('{0}中最大值为{1}'.format(numList, max(numList)))
    print('{0}中最大值为{1}'.format(numSet, max(numSet)))


"""14.判断质数"""
def judge_primenum():
    print('判断质数游戏，输入结束停止运行，输入其他继续!')
    while True:
        num = input('请输入正整数:')
        flag = num.isdigit()
        if num == '结束':
            print('游戏结束')
            break
        elif flag:
            num = int(num)
            if num > 1:
                for i in range(2, num):
                    if num % i == 0:
                        print('{0}是合数，因数为{1}'.format(num, i))
                        break
                else:
                        print('{0}是质数'.format(num))
            else:
                print('{0}不是质数'.format(num))
        else:
            print('输入的不是正整数')


"""15.输入指定范围的素数"""
def Prime_number():
    print("输出指定范围内的素数，输入结束结束游戏，输入其他继续！")
    while True:
        min, max = input('输出区间最小值：'), input('输出区间最大值：')
        flag1 = min.isdigit()
        flag2 = max.isdigit()               # isdigit()判断输入是否为正整数方法，正确返回True，否则返回False
        if min == '结束' or max == '结束':  # 控制游戏结束
            break
        elif flag1 and flag2:               # 判断输入的数正确后，开始进入素数计算
            min, max = int(min), int(max)
            if max < min:
                print('最大值小于最小值，请重新输入！')
                continue
            for i in range(min, max+1):
                if i < 2:                   # 素数是大于1的自然数，这个判断用来去除0和1
                    continue
                for j in range(2, i):
                    if i % j == 0:
                        break
                else:
                    print(i, ' ', end='')
            print('')
        else:
            print('输入的不是正整数，请重新输入！')


"""16.1.阶乘，通过for循环算阶乘（相对python自带阶乘方法计算速度慢一些）"""
def factorial_slow():
    print('求出输入的正整数的阶乘游戏，输入结束终止游戏，输入其他继续！')
    while True:

        num = input('输入正整数:')
        flag = num.isdigit()
        if num == '结束':
            print('游戏结束！')
            break
        elif flag:
            num = int(num)
            if num == 0:
                print('{0}的阶乘是1'.format(num))
            else:
                product = 1
                start = time.time()
                for i in range(1, num+1):
                    product = product * i
                print('{0}的阶乘是{1}'.format(num, product))
                end = time.time()
                print('运算时间：{0:.2f}'.format(end - start))
        else:
            print('输入的数不是正整数，请重新输入!')
    pass


"""16.2.阶乘，调用math库的阶乘方法"""
def factorial_fast():
    print('求出输入的正整数阶乘游戏，输入结束终止游戏，输入其他继续！')
    while True:
        num = input('输入正整数:')
        flag = num.isdigit()
        if num == '结束':
            print('游戏结束!')
            break
        elif flag:
            num = int(num)
            start = time.time()
            product = factorial(num)                # 调用math库的factorial方法，计算阶乘
            print('{0}的阶乘是{1}'.format(num, product))
            end = time.time()
            print('计算时间:{0:.2f}'.format(end-start))
        else:
            print('输入的不是正整数，请重新输入！')


"""17.九九乘法表"""
def multipyl_table():
    print('九九乘法表')
    for i in range(1, 10):
        for j in range(1, i+1):
            if i == j:                              # 判断当为一行中最后一个时，输入结果是带换行
                print('{}*{}={}'.format(j, i, i*j))
            else:                                   # 同一行的乘法不换行，空格结尾
                print('{}*{}={}'.format(j, i, i * j), end='\t')


"""18.1菲波那契数列，自由选择输出多少数据"""
def fibonacci_seq():
    print('斐波那契数列游戏，输入结束终止游戏，输入其他继续!')
    while True:
        num = input('需要输出几项：')
        flag = num.isdigit()
        if num == '结束':
            print('游戏结束')
            break
        elif flag:
            num = int(num)
            fibo = [0, 1]
            if num == 0:
                print('{}不是正整数，请重新输入!'.format(num))
                continue
            elif num == 1:
                print('斐波那契数列:[{}]'.format(fibo[0]))
            elif num == 2:
                print('斐波那契数列:{}'.format(fibo))
            else:
                for i in range(2, num):
                    m = fibo[i-2] + fibo[i-1]
                    fibo.append(m)
                print('斐波那契数列:{}'.format(fibo))
        else:
            print('输入的不是正整数，请重新输入!')


"""18.2斐波那契数列，输入一个数字，输出范围内的斐波那契数列"""
def fibonacci_num():
    print('输入目标数字，计算出范围内的数列后输出，输入结束终止游戏，输入其他继续!')
    while 1:
        num = input('输入目标数字:')
        flag = num.isdigit()
        if num == '结束':
            print('游戏结束!')
            break
        elif flag:
            num = int(num)
            a, b = 0, 1
            fibo = [0, 1]       # 斐波那契数列前两位为0,1
            while 1:
                if a+b <= num:
                    fibo.append(a+b)    # 斐波那契数列规则：当前数等于前两位数之和（从第3位起），append把斐波那契数写入数列中
                    a, b = b, a+b       #
                else:
                    break
            if num == 0:
                print('[{}]'.format(fibo[0]))
            else:
                print(fibo)
        else:
            print('输入的不是正整数，请重新输入!')


"""18.3斐波那契数列，简易版输出范围内的斐波那契数列"""
def fibonacci_numTwo():
    print('斐波那契数列游戏，输入目标数字计算出范围内的数列后输出，输入结束终止游戏，输入其他继续!')
    while 1:
        num = input('输入目标数字:')
        flag = num.isdigit()
        if num == '结束':
            print('游戏结束!')
            break
        elif flag:
            num = int(num)
            a, b = 0, 1
            while a <= num:
                print(a, end=' ')
                a, b = b, a+b
            print()
        else:
            print('输入的数据有误，请重新输入!')


"""19.1阿姆斯特朗数，判断输入的数是否为阿姆斯特朗数"""
def armstrong_num():
    print('判断输入的数是否为阿姆斯特朗数游戏，输入结束终止游戏，输入其他继续!')
    while 1:
        num = input('输入正整数：')
        flag = num.isdigit()
        if num == '结束':
            print('游戏结束!')
            break
        elif flag:
            n = len(num)            # 计算长度来得知是几位数
            num = int(num)
            # m = len(str(num))     # 整型数字可通过先转化为str类型，在计算长度得知是几位数
            tnum = num
            sum = 0
            if num == 0:
                print('0不是正整数，请重新输入!')
                continue
            for i in range(0, n):    # 阿姆斯特朗数特质：一个n位整数等于它各个数的n次方的和，如1^3+5^3+3^3=153
                digit = tnum % 10    # 取出个位数
                sum += digit ** n    # 取出的数字次方后求和
                tnum //= 10          # 整除10，把第二位数变成个数，继续取出个位数求和，//整除符号，结果不带小数点
            if num == sum:
                print('{}是阿姆斯特朗数'.format(num))
            else:
                print('{}不是阿姆斯特朗数'.format(num))

        else:
            print('输入的不是正整数')


"""19.2阿姆斯特朗数，计算出范围内的阿姆斯特朗数"""
def armstrong_seq():
    print('计算出范围内的阿姆斯特朗数，输入结束终止游戏，输入其他继续!')
    while True:
        min = input('请输入最小范围:')
        num = input('请输入最大范围:')
        flag1, flag2 = num.isdigit(), min.isdigit()
        if num == '结束' or min == '结束':
            print('游戏结束!')
            break
        elif flag1 and flag2:
            num = int(num)
            min = int(min)
            smr = []
            if min < 1:
                print('请输入大于0的正整数!')
                continue
            elif min > num:
                print('最大范围需大于或等于最小范围，请重新设置!')
                continue
            for i in range(min, num+1):
                n = len(str(i))
                tnum = i
                sum = 0
                for j in range(0, n):
                    digit = tnum % 10
                    sum += digit ** n
                    tnum //= 10
                if i == sum:
                    smr.append(i)
            print('{}-{}范围内的阿姆斯特朗数：{}'.format(min, num, smr))

        else:
            print('输入的不是正整数，请重新输入!')


"""20.十进制转换成二进制、八进制、十六进制"""
def decimal_change():
    print('十进制转换成二、八、十六进制游戏，输入结束终止游戏，输入其他继续!')
    while 1:
        num = input('输入十进制数：')
        flag = public.isdigit_two(num)
        if num == '结束':
            print('游戏结束!')
            break
        elif flag:
            num = int(num)
            while 1:
                type = input('请选择转换的类型(输入二、八、十六转换成对应的进制),输入返回回到上一层:')
                if type == '返回' or type == '结束':
                    print('返回成功', end=',')
                    break
                elif type == '二' or type == '2':
                    num_binary = bin(num)               # bin()方法，将十进制装换为二进制
                    num_int = int(num_binary, 2)           # int(obj，进制数)方法，可将二、八、十六进制数转为十进制数
                    print('二进制数\033[1;34m{}\033[0m转化十进制数为:\033[1;31m{}\033[0m'.format(num_binary, num_int))

                    # \033[1;34m：设置后面文字颜色，\033[固定格式，1显示方式，34m显示颜色，详情查看config库
                    print('\033[1;34m{}\033[0m转化成二进制为:\033[1;34m{}\033[0m'.format(num, num_binary))
                    continue
                elif type == '八' or type == '8':
                    num_octal = oct(num)                # oct()方法，将十进制装换成八进制
                    print('\033[1;34m{}\033[0m转化成八进制为:\033[1;34m{}\033[0m'.format(num, num_octal))
                    continue
                elif type == '十六' or type == '16':
                    num_hex = hex(num)                  # hex()方法，将十进制装换成十六进制
                    print('\033[1;34m{}\033[0m转化成十六进制为:\033[1;34m{}\033[0m'.format(num, num_hex))
                    continue
                else:
                    print('\033[1;41m不支持此类型转换，请重新输入!\033[0m')
                    continue
        else:
            print('\033[1;31m输入的不是十进制数，请重新输入!\033[0m')


"""21.ASCII码与字符相互转换"""
def ascii_char():
    print('ASCII码与字符相互转换游戏，输入结束终止游戏，输入其他继续!')
    while 1:
        sele = input('输入1 ASCII码转字符,输入2 字符转ASCII码,输入结束终止游戏:')
        if sele == '结束':
            print('结束游戏!')
            break
        elif sele == '1':
            while True:
                asc = input('输入ASCII码(输入返回回到上一层):')
                flag = asc.isdigit()
                if (asc == '返回') | (asc == '结束'):
                    print('返回成功', end=',')
                    break
                elif flag:
                    asc = int(asc)
                    if asc > 1114111:
                        print('没有此ASCII码，请重新输入!')
                    else:
                        char = chr(asc)

                        # 存疑：ascii码55555时报编码错误，之后解决
                        print('ASCII码\033[1;31m{}\033[0m转化字符为:\033[1;31m{}\033[0m'.format(asc, char))
                else:
                    print('没有此ASCII码，请重新输入!')

        elif sele == '2':
            while True:
                char = input('输入字符(输入返回回到上一层):')
                num = len(char)
                if (char == '返回') | (char == '结束'):
                    print('返回成功', end=',')
                    break
                elif num == 1:
                    asc = ord(char)
                    print('字符\033[1;31m{}\033[0m转化ASCII码为:\033[1;31m{}\033[0m'.format(char, asc))
                else:
                    print('输入有误，请重新输入!')

        else:
            print('没有此选项，请重新选择!')


"""22.1最大公约数"""
def divisor_maxnum():

    # divi = gcd(10, 20)         # gcd()方法，python内部库计算最大公约数方法
    print('求两个数最大公约数，输入结束终止游戏，输入其他继续!')
    a = input('输入第一个数:')
    b = input('输入第二个数:')
    i = 0
    while 1:
        flag1, flag2 = a.isdigit(), b.isdigit()
        if (a == '结束') | (b == '结束'):
            print('游戏结束!')
            exit()              # 结束整个程序，退出主函数
            # break             # 本方法使用了递归函数，递归后使用break退出会多循环一次，所以本次使用exit()方法退出
        if (not flag1) | (a == '0'):
            a = input('第一个数输入有误,请重新输入:')
        if (not flag2) | (b == '0'):
            b = input('第二个数输入有误，请重新输入:')
        elif flag1 & flag2:
            a, b = int(a), int(b)
            m, n = 0, 0
            m, n = a, b
            min_num = min(a, b)
            max_num = max(a, b)
            divisor = 1
            div_seq = [1]
            if max_num % min_num == 0:
                print('\033[1;34m{}\033[0m和\033[1;34m{}\033[0m的最大公约数为:\033[1;34m{}\033[0m'.format(a, b, min_num))
            else:
                for i in range(2, (min_num//2)):       # 最大公约数求法，求两个数最大可整除的数，循环次数设置为最小数的数值
                    while True:
                        if (m % i == 0) & (n % i == 0):  # 循环去找到满足两个数都能整除的数
                            m = m // i
                            n = n // i
                            divisor *= i                # 所有能整除的约数相乘，求出最大公约数
                            div_seq.append(i)           # 所有公约数写入列表
                        else:
                            break
                print('\033[1;34m{}\033[0m和\033[1;34m{}\033[0m的最大公约数为:\033[1;34m{}\033[0m'.format(a, b, divisor))
                print('\033[1;34m{}\033[0m和\033[1;34m{}\033[0m的所有公约数为:\033[1;34m{}\033[0m'.format(a, b, div_seq))
            divisor_maxnum()        # 递归，调用本函数再次使用


"""22.2最大公约数，欧几里算法(通过求余方式得出最大公约数)"""
def divisor_maxnum2():
    print('求两个数最大公约数，输入结束终止游戏，输入其他继续!')
    a = input('输入第一个数:')
    b = input('输入第二个数:')
    i = 0
    while 1:
        flag1, flag2 = a.isdigit(), b.isdigit()
        if (a == '结束') | (b == '结束'):
            print('游戏结束!')
            exit()  # 结束整个程序，退出主函数
            # break             # 本方法使用了递归函数，递归后使用break退出会多循环一次，所以本次使用exit()方法退出
        if (not flag1) | (a == '0'):
            a = input('第一个数输入有误,请重新输入:')
        if (not flag2) | (b == '0'):
            b = input('第二个数输入有误，请重新输入:')
        elif flag1 & flag2:
            a, b = int(a), int(b)
            m, n = 0, 0
            m, n = a, b
            while b != 0:
                a, b = b, a % b
            print('\033[1;34m{}\033[0m和\033[1;34m{}\033[0m的最大公约数为:\033[1;34m{}\033[0m'.format(m, n, a))
            divisor_maxnum2()  # 递归，调用本函数再次使用


"""22.3求多个数的最大公约数"""
def divisor_munum():
    print('求多个数的最大公约数，输入结束停止运行，输入其他继续!')
    while 1:
        num = input('输入要检测的数字，如(5,25,75):')
        num = re.split(r'[,，]', num)            # 通过re.split('[分隔符号]', 字符串对象)方法，可通过多个分割符分割字符串
        num_list, appro_list, divi_list = [], [], []
        j = 0
        for i in num:               # 1.输入的整数存入num_list的列表中
            flag = i.isdigit()
            if i == '结束':
                print('游戏结束!')
                exit()
            elif flag:
                if i == '0':
                    print('0不是正整数，请重新输入!')
                    break
                num_list.append(int(i))
            else:
                print('输入的不是正整数，请重新输入!')
                break
            j += 1
        if j == len(num):
            for i in num_list:              # 2.求出每个数的所有约数，包括本身，存入appro_list列表中
                for j in range(1, 1+i):
                    if i % j == 0:
                        appro_list.append(j)

            # 3.判断appro_list列表中约数相同的数的个数检测数字的个数对比，相同则次数为几个数字的公约数，并存人divi_list列表中
            for i in appro_list:
                if appro_list.count(i) == len(num_list):
                    # print(i)
                    divi_list.append(i)

            # print('公约数为:{}'.format(divi_list))
            print('{}的最大公约数为:{}'.format(num_list, max(divi_list)))  # max(divi_list),求出公约数列表中最大数，此数即是最大公约数


"""23.1两数的最小公倍数"""
def multiple_minnum():

    # multi = lcm(10, 20)   # lcm()方法，python自带库计算两数最小公倍数方法
    print('求两数的最小公倍数游戏,输入结束终止游戏，输入其他继续!')
    a = input('输入第一个数:')
    b = input('输入第二个数:')
    while True:

        flag1, flag2 = a.isdigit(), b.isdigit()
        if (a == '结束') | (b == '结束'):
            print('\033[1;32m游戏结束!\033[0m')
            exit()
        elif (not flag1) | (a == '0'):
            a = input('第一个数输入有误，请重新输入:')
        elif (not flag2) | (b == '0'):
            b = input('第二个数输入有误，请重新输入:')
        else:
            a, b = int(a), int(b)
            m , n = a, b
            mult = []
            max_num = max(a, b)
            if (max_num % a == 0) & (max_num % b == 0):
                print('{}和{}的最小公倍数为:{}'.format(a, b, max_num))
                multiple_minnum()

            # 方法1（运算较慢）原理：最小公倍数大于等于两数最大值，小于等于两数乘积，在此范围内找出两数所有公倍数，再找出其中最小的
            # for i in range(max_num, (a * b) + 1):
            #     if (i % a == 0) & (i % b == 0):
            #         mult.append(i)
            #
            # print('{}和{}的最小公倍数为:{}'.format(a, b, min(mult)))

            # 方法2(运算较快)原理：最小公倍数与最大公约数乘积等于两数的乘积，先求出两数最大公约数，通过欧几里方法求出最大公约数，再得出最小公倍数
            while b != 0:
                a, b = b, a % b
            mult_min = (m * n) // a
            print('\033[1;34m{}\033[0m和\033[1;34m{}\033[0m的最小公倍数为:\033[1;34m{}\033[0m'.format(m, n, mult_min))
            multiple_minnum()


"""23.2求多个数的最小公倍数"""
def multiple_mumin():
    print('求多个数的最小公倍数，输入结束停止运行，输入其他继续!')
    while True:
        num = input('输入需要计算的数字(如:5,25,75):')
        num = re.split('[,，]', num)
        num_list, num2_list = [], []
        j = 0
        for i in num:
            flag = i.isdigit()
            if i == '结束':
                print('\033[1;32m游戏结束!\033[0m')
                exit()
            elif flag:
                i = int(i)
                if i == 0:
                    print('\033[1;31m请输入大于0的正整数!\033[0m')
                    break
                num_list.append(i)
            else:
                print('输入有误，请重新输入!')
                break
            j += 1
        if j == len(num):
            num2_list = list(num_list)      # list()方法，复制num_list列表
            mult = num_list[0]              # 存放公倍数
            var = num_list[0]               # 临时存储数据
            for i in range(1, j):
                while num_list[i] != 0:
                    var, num_list[i] = num_list[i], var % num_list[i]
                mult = (mult * num2_list[i]) // var
                var = mult                  # 临时存储前面两数的最小公倍数，用来计算与下一个数的最小公倍数

            print('\033[1;34m{}\033[0m的最小公倍数为:\033[1;34m{}\033[0m'.format(num2_list, mult))


"""24.简易计算器实现"""
def simple_calculator():
    print('简易计算器实现，输入结束终止游戏，输入其他继续!')
    while 1:
        oper = input('输入数字，选择运算方法(1:加;2:减;3:乘;4:除):"')
        # a = input('输入第一个数:')
        # b = input('输入第二个数:')
        flag = oper.isdigit()
        if oper == '结束':
            print('游戏结束!')
            break
        elif flag:
            while True:
                if (oper == '1') | (oper == '2') | (oper == '3') | (oper == '4'):
                    a = input('输入第一个数:')
                    b = input('输入第二个数:')
                    flag1, flag2 = public.isdigit(), b.isdigit()
                    if flag1 & flag2:
                        a, b = int(a), int(b)
                    else:
                        print('')
                else:
                    print('没有此运算方法，请重新输入')
                    break
        else:
            print('没有此运算方法，请重新输入')


"""主函数"""
def main():
    number_sum()
    square_Root()
    square_Root2()
    # equation()
    Triangle_area()
    Round_area()
    Type_assert()
    get_random()
    temperature()
    switch()
    if_else()
    judge_number()
    odd_or_even()
    judge_leapyear()
    max_num()
    judge_primenum()
    fibonacci_seq()
    fibonacci_num()
    fibonacci_numTwo()
    armstrong_num()
    armstrong_seq()
    decimal_change()
    ascii_char()
    divisor_maxnum()
    divisor_maxnum2()
    divisor_munum()
    multiple_minnum()
    multiple_mumin()

    # 循环控制方法
    # flag = True
    # while flag:
    #     Type_assert()
    #     e = input('输入end结束循环，输入其他继续：')
    #     if e == 'end':
    #         break


if __name__ == '__main__':

    # main()
    # multipyl_table()
    # fibonacci_seq()


    """列表复制方式"""
    # n, m = [10, 20, 30], []
    # m = n[:]                      # 1.通过切片方法，创建新的列表，:冒号前后可放入索引，不放入索引代表切到列表末尾
    # m = list(n)                   # 2.list()构造函数，可读性高的方法
    # m = n * 1
    # m = copy.copy(n)
    # m = copy.deepcopy(n)            # 子表和父表同时复制
    # for i in range(0, 2):
    #     n[i], n[i+1] = n[i+1], n[i] % n[i+1]
    # print(id(m), id(n))     # id()方法，查看对象的内存地址，发现两个数列内存地址一致，所以修改其中一个数列相当于修改两个了
    # print(m, n)

    """编码调试"""
    # num = 55555
    # char = chr(num)
    # # print(char)
    # char = char.encode(encoding='utf-8')
    # print(chardet.detect(char))
    # print(char)
    # while 1:
    #     num = input('请输入').split(',')
    #     k = []
    #     j = 0
    #     for i in num:
    #         flag = i.isdigit()
    #         if i == '结束':
    #             print('游戏结束!')
    #             exit()
    #         elif flag:
    #             if i == '0':
    #                 print('0不是正整数，请重新输入!')
    #                 break
    #             k.append(int(i))
    #         else:
    #             print('输入的不是正整数，请重新输入!')
    #             break
    #         j += 1
    #     if j == len(num):
    #         print(k)
    for i in range(5):
        for j in range(5):
            if j >= 4-i:
                print('*', end="")
                continue
            if j < 2-i:
                print(' ', end="")
        print('')


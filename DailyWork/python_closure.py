# _*_ config: utf-8 _*_
# python 闭包

# 闭包1，使用外部函数传入的变量
def closure_one(num):
    # 在函数内部定义一个函数，且这个函数使用了外部函数的变量，那么将用到的函数和变量称之为闭包
    def closure_one_in(num_in):
        print(num_in)
        # 返回闭包的结果
        return num + num_in
    # 返回闭包函数(即返回闭包的结果)
    return closure_one_in

# 闭包2，引用外部函数作用域的变量(非全局变量)
def closure_tow(num, num2):
    data_list = [num, num2]

    # 使用外部作用域变量，内部函数则为闭包
    def closure_tow_in():
        data_list[0] += 1
        return data_list
    return closure_tow_in

def closure_three(num):

    def closure_three_in():
        # nonlocal访问外部函数局部变量
        nonlocal num
        num += 1
        return num
    return closure_three_in


if __name__ == '__main__':

    # 闭包思考:
    #          1.闭包似优化了变量，原来需要类对象完成的工作，闭包也可以完成
    #          2.由于闭包引用了外部函数的局部变量，则外部函数的局部变量没有及时释放，消耗内存
    # print(closure_one(10)(20))
    # print(closure_tow(10, 20)())
    closure = closure_one(10)
    print(closure(20))
    print(closure(20))




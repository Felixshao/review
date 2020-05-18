# _*_ config: utf-8 _*_
# python迭代器和生成器


def python_iterator():
    """python自带迭代器方法：iter"""
    data_list = [1, 2, 3, 4, 5]
    it = iter(data_list)    # list对象转换为迭代器
    print(next(it))     # next方法获取迭代器值
    print(next(it))
    for x in it:    # 循环方法获取迭代器值
        print('x: ', x)


# 生成器
fei = []
def feibonaqi():
    """生成斐波那契数列迭代器"""
    for i in range(20):
        if i > 1:
            fei.append(fei[i-1] + fei[i-2])
        else:
            fei.append(i)
        yield fei[i]


if __name__ == '__main__':
    bona = feibonaqi()

    for i in bona:
        print(i)

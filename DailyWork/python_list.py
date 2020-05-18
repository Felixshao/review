# _*_ config: utf-8 _*_
# python3的列表

def takeSecond(elem):
    return elem[0]

def takedict(dict):
    return dict['num']


list_one = [10, 25, 10, 3, 50, 14, 24]
list_second = [[1, 2], [5, 3], [9, 10], [2, 6], [8, 7]]
list_dict = [{'num': 1}, {'num': 2}, {'num': 5}, {'num': 4}, {'num': 6}]
list_one.sort()  # 升序
print(list_one, '内存地址:', id(list_one))
list_one.sort(reverse=True)     # 降序
print(list_one, '内存地址:', id(list_one))
list_second.sort(key=takeSecond)
print(list_second, '内存地址:', id(list_one))
list_second.sort(key=lambda el: el[1])
print(list_second, '内存地址:', id(list_one))
list_second.sort(key=takeSecond, reverse=True)
print(list_second, '内存地址:', id(list_one))
list_dict.sort(key=takedict, reverse=True)  # 根据指定嵌套字典的值升序排序
print(list_dict, '内存地址:', id(list_one))
list_dict.sort(key=lambda lidi: lidi['num'], reverse=False)     # 根据指定嵌套字典的值降序排序
print(list_dict, '内存地址:', id(list_one))

print(list_second)
one = lambda le: le[1]  # lambda函数

print(one(list_second))

*one, num = list_one    # *号表达式，可存储列表/可迭代变量多个值
print(*one, '\n', num)

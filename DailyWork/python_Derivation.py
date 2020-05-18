# _*_ config: utf-8 _*_

def list_derivation():
    """list推导式学习"""

    # 简单推导式
    nums = [i**2 for i in range(10)]
    print(nums)

    # 复杂推导式
    nums2 = [j for i in range(10) for j in range(i)]
    print(nums2)

    # 推导式可读性
    nums2_norm = [
        j
        for i in range(10)
        for j in range(i)
    ]
    print(nums2_norm)

    # 推导式冒泡排序实例
    fraction = [10, 50, 20, 100, 88, 45, 30, 80]
    fraction2 = [
        i**i
        for i in range(10)
    ]
    print(fraction2)


def dict_derivation():
    """dict推导式学习"""
    # 推导式字典键值互换
    dict_data = {'姓名': 'shao', '年龄': '12'}
    dict_data = {value: key for key, value in dict_data.items()}
    print(dict_data)

    # 推导式，两list合并字典
    list_key = ['姓名', '年龄']
    list_value = [['shao', 12]]
    dict_data = {
        list_key[key]: list_value[value][key]
        for value in range(len(list_value))
        for key in range(len(list_key))
    }
    print(dict_data)


def set_derivation():
    """set推导式学习"""
    # 用一个列表的所有单词的首字母生成一个集合
    words_list = 'words'
    chars = {w for w in words_list}
    print(chars)


if __name__ == '__main__':
    list_derivation()
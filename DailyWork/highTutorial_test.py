import unittest
import re


class high_case(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        print('开始\n')

    @classmethod
    def tearDownClass(cls):

        print('结束\n')

    """1.正则表达式匹配数据"""
    def test1_Regular1(self):

        str = '<div class="dis_inlblo"><span class="rank_table_name">charlesUI</span><div class="dis_inlblo"><span class="rank_table_name">charlesUI2</span>'
        # re.match方法使用正则匹配字符串,从字符串开头匹配，开头不匹配直接返回none，
        # pattern参数：放入正则表达式，string参数：放入匹配的字符串
        # flags参数：放入修饰符，如re.M(多行匹配)，re.I(不区分大小写)
        # ()框起来的正则为一个组，可以通过group()方法取出
        regular = re.match(pattern='<div class="dis_inlblo"><span class="rank_table_name">(.*)</span>', string=str, flags=re.M)

        # print(regular.group())      # 通过group方法获取所有匹配的数据
        # print(regular.group(3))     # 通过传入数字，获取匹配的组
        # list = []
        print(regular.group(1))
        # for i in regular.group():
        #
        #     print()
        #
        # print(list)

    """2.正则表达式compile方法"""
    def test2_compile(self):
        str = '<div class="dis_inlblo"><span class="rank_table_name">charlesUI</span>\n' \
              '<div class="dis_inlblo"><span class="rank_table_name">charlesUI2</span>'
        str1 = '<a>123</a> \n <a>大侠</a>'
        # re.compile方法,pattern参数传入正则表达式， flags参数传入匹配模式：如re.I(获取大小写)、re.M(多行模式)等
        # findall方法，找到所有子串，返回list，无结果返回空.string参数:传入需要匹配的字符串， pos:起始位置，默认0， endpos:结束的位置
        regular = re.compile(pattern='<a>(.*)</a>')
        resu = regular.findall(string=str1)
        print(resu)




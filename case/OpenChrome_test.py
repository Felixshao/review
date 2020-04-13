# -*- coding: utf-8 -*-
# @Time     : 2019.4
# @Author   : felix
# @Email    : shaoyufei1234@163.com
# @File     : .py
# @Software : PyCharm


from selenium import webdriver


def openChrome():

    su = webdriver.Chrome()
    su.get('https://www.baidu.com')


if __name__ == '__main__':

    openChrome()
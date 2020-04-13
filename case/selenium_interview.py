# -*- coding: utf-8 -*-
# @Time     : 20199.10
# @Author   : felix
# @Email    : shaoyufei1234@163.com
# @File     : selenium_intetrview.py
# @Software : PyCharm

from selenium import webdriver
from time import sleep

# 面试+笔试题
"""1.selenium如何判断元素是否存在"""
def elem_presence():
    open_chrome()
    driver.isElementExist()


"""主函数，打开浏览器"""
def open_chrome():
    driver = webdriver.Chrome()
    global driver
    driver.get('https://www.baidu.com')
    driver.maximize_window()
    # driver.implicitly_wait(10)


if __name__ == '__main__':

    open_chrome()
    pass

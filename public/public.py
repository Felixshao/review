# -*- coding: utf-8 -*-
# @Time     : 2019.4
# @Author   : felix
# @Email    : shaoyufei1234@163.com
# @File     : .py
# @Software : PyCharm
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


"""判断字符串是否为数字方法,认定小数、正数、负数为数字"""
def isdigit(x):
    """
    是数字返回True，否返回False
    """
    try:
        x = float(x)                    # 将字符串转为float型
        return isinstance(x, float)     # isinstance方法判断字符串是否为此类型，正确返回True，错误返回False
    except ValueError:
        return False


"""判断字符串是否为数字方法,认定正整数、负整数为数字"""
def isdigit_two(x):
    """
    是数字返回True，否返回False
    """
    try:
        x = int(x)                    # 将字符串转为float型
        return isinstance(x, int)     # isinstance方法判断字符串是否为此类型，正确返回True，错误返回False
    except ValueError:
        return False

def WeddriverWait_Textclick(driver, element):
    """

    :param driver:
    :param type: 定位元素的方式；例：By.ID
    :param element:link_text文本
    :return:
    """
    try:
        WebDriverWait(driver, 6, 0.5).until(EC.element_to_be_clickable((By.LINK_TEXT, element)), message="找不到元素或元素无法点击")
        flag = True
    except BaseException as b:
        print(b)
        flag = False

    if flag:
        driver.find_element_by_link_text(element).click()

def WeddriverWait_Xpathclick(driver, element):
    """

    :param driver:
    :param type: 定位元素的方式；例：By.ID
    :param element:xpath
    :return:
    """
    try:
        WebDriverWait(driver, 6, 0.5).until(EC.element_to_be_clickable((By.XPATH, element)), message="找不到元素或元素无法点击")
        flag = True
    except BaseException as b:
        print(b)
        flag = False

    if flag:
        driver.find_element_by_xpath(element).click()



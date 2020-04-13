import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# 面试+笔试题
class B_class(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('C:/Users/felix/Desktop/百度一下，你就知道.html')
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        sleep(3)
        pass

    """1.selenium如何判断元素是否存在？"""
    """2.selenium中hidden或者是display ＝ none的元素是否可以定位到？"""
    def test1_1elem(self):
        driver = self.driver

        # execute_script()同步执行js代码方法，修改display='none'(不显示)属性为'block'（显示/块状化）
        driver.execute_script("document.getElementById('kw').style.display='block';")

        # driver.execute_script('arguments[0].setAttribute('style',arguments[1]);",'kw',
        #                   "display:'block';')
        t1 = driver.find_elements_by_id('kw')  # elements,查找多个元素返回列表，找不到不报错，返回为空列表
        print(t1)
        if len(t1) > 0:                             # 通过列表是否为空判断元素是否存在
            t1[0].send_keys('123')                  # 返回的列表不能直接使用send_keys()方法，需指定某个值
            flag = True
        else:
            flag = False
        print(flag)

        try:                                    # 使用try except方法判断页面是否存在此元素，存在返回True，否则False
            t2 = driver.find_element_by_id('kw').send_keys('123')
            flag = True
        except:
            flag = False
        print(flag)
        # if flag is True:
        # t1[0].send_keys('123')

        # t1.send_keys('123')

    """3.WebDriverWait(),显示等待"""
    def test_webdriverwait(self):
        driver = self.driver
        t1 = driver.find_element_by_id('kw')
        print(t1.is_displayed())            # is_displayed()方法，查看元素是否可见
        try:
            WebDriverWait(self.driver, 5).until(lambda the_driver: the_driver.find_element_by_id('kw1').is_displayed(), '失败')
        except BaseException as b:
            print(b)






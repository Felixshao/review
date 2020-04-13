import unittest
from selenium import webdriver


class four18_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.dr = webdriver.Chrome()
        cls.dr.get('https://www.baidu.com')
        cls.dr.maximize_window()
        cls.dr.implicitly_wait(10)

    def test1_open(self):

        text = self.dr.find_element_by_id('su').get_attribute('value')  # get_attribute获取元素属性值
        print(text)

    @classmethod
    def tearDownClass(cls):

        cls.dr.quit()
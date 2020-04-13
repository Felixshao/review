import unittest
from selenium import webdriver
from time import sleep

class Bcase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.md = webdriver.Chrome()        # 打开谷歌
        cls.md.maximize_window()
        cls.md.get('https://www.baidu.com')     # 打开百度
        cls.md.implicitly_wait(8)

    @classmethod
    def tearDownClass(cls):

        cls.md.quit()

    def test1_search(self):

        md = self.md
        md.find_element_by_id('kw').send_keys('123')
        print('test1结束')

    def test2_search2(self):

        md = self.md
        md.find_element_by_link_text('图片').click()
        print('test2结束')


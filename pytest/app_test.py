import unittest
from appium import webdriver
from time import sleep

class Bcase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """微信app配置"""
        desired_caps2 = {
            'appium_url': 'http://127.0.0.1:4723/wd/hub',
            'platformName': 'Android',
            'platformVersion': '9',
            'deviceName': 'c09714bd',
            'appPackage': 'com.tencent.mm',
            'appActivity': '.ui.LauncherUI',
            # 'automationName': 'uiautomator2',
            # 'autoAcceptAlerts': True,
            'noReset': True,
            'noSign': True,
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'},
            'newCommandTimeout': 30,  # 超过30s无下个命令，退出
            # 'chromedriverExecutable': 'F:\\test\\chromeDriver\\2.37\\chromedriver.exe'
        }

        cls.md = webdriver.Remote(desired_caps2['appium_url'], desired_caps2)        # 打开谷歌
        cls.md.implicitly_wait(8)

    @classmethod
    def tearDownClass(cls):

        cls.md.quit()

    def test1_search(self):

        print('打开微信')
        sleep(3)


if __name__ == '__main__':

    unittest.main()



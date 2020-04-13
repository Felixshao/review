import unittest
import time
import os, signal
import subprocess
from time import sleep
from appium import webdriver
from appium.webdriver.mobilecommand import MobileCommand


class app_case(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        """懂车帝app"""
        desired_caps = {
            'appium_url': 'http://localhost:4723/wd/hub',   # appium服务器地址
            'platformName': 'Android',                      # 设备操作系统
            'platformVersion': '9',                         # 设备系统版本
            'deviceName': 'c09714bd',                       # 远程连接的设备名称
            'appPackage': 'com.ss.android.auto',            # 启动的app包名
            'appActivity': '.activity.SplashActivity',      # app首个activity
            'noReset': True,                                # 启动时不重置（清除）app原有数据
            'noSign': True,                                 # 跳过对应用的签名
            'unicodeKeyboard': True,                        # 使用Unicode输入法
            'resetKeyboard': True,                          # 结束后恢复默认输入法
            'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'},    # 需要切换到webview时加入此配置，value值为webview的context
            'newCommandTimeout': 30,  # 超过30s无下个命令，退出
        }

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
            'chromeOptions':  {'androidProcess': 'com.tencent.mm:tools'},
            'newCommandTimeout': 30,       # 超过30s无下个命令，退出
            # 'chromedriverExecutable': 'F:\\test\\chromeDriver\\2.37\\chromedriver.exe'
        }

        """掌上联盟app配置"""
        desired_caps3 = {
            'appium_url': 'http://127.0.0.1:4723/wd/hub',
            'platformName': 'Android',
            'platformVersion': '9',
            'deviceName': 'c09714bd',
            'appPackage': 'com.tencent.tgp',
            'appActivity': 'com.tencent.wegame.splash.SplashActivity',
            # 'automationName': 'uiautomator2',
            # 'autoAcceptAlerts': True,
            'noReset': True,
            'noSign': True,
            'unicodeKeyboard': True,
            'resetKeyboard': True,
        }

        """微信app配置"""
        desired_caps4 = {
            'appium_url': 'http://127.0.0.1:4723/wd/hub',
            'platformName': 'Android',
            'platformVersion': '9',
            'deviceName': 'c09714bd',
            'appPackage': 'cn.nubia.browser',
            'appActivity': 'com.android.browser.BrowserLauncher',
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

        """仁链app配置"""
        desired_caps5 = {
            'appium_url': 'http://127.0.0.1:4723/wd/hub',
            'platformName': 'Android',
            'platformVersion': '9',
            'deviceName': 'c09714bd',
            'appPackage': 'com.pumpkinstudy.kind',
            'appActivity': '.activity.StartUpActivity',
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

        """TGP app配置"""
        desired_caps6 = {
            'appium_url': 'http://127.0.0.1:4723/wd/hub',
            'platformName': 'Android',
            'platformVersion': '9',
            'deviceName': 'c09714bd',
            'appPackage': 'com.tencent.tgp',
            'appActivity': 'com.tencent.wegame.splash.SplashActivity',
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

        # cls.app = webdriver.Remote(desired_caps5['appium_url'], desired_caps5)
        # cls.app.implicitly_wait(8)
        # cls.app.background_app(2)  # background_app()方法，使app后台运行,作用:防止app启动后activity卡在启动页上，导致后续元素无法定位
        pass

    @classmethod
    def tearDownClass(cls):
        sleep(5)
        # cls.app.quit()
        pass

    def test1_car(self):
        app = self.app
        app.find_element_by_id('android:id/tabs')
        # app.find_elements_by_id('com.ss.android.auto:id/brs')[1].click()        # 选择选车目录
        # 选择选车目录,find_element_by_android_uiautomator("new UiSelector().text(\"定位的文本内容\")")方式定位文本内容
        text = app.find_element_by_android_uiautomator('new UiSelector().text(\"选车\")').click()
        app.find_elements_by_id('com.ss.android.auto:id/alq')[5].click()    # 选择车排行第一个

        car_acti = app.current_activity     # 获取activity
        app.find_elements_by_id('com.ss.android.auto:id/j1')[0].click()     # 选择第一辆车

        size = app.get_window_size()
        width = size['width']
        height = size['height']

        # 向上滑动屏幕
        for i in range(3):
            x = width * 0.5
            y1 = height * 0.8
            y2 = height * 0.2
            app.swipe(x, y1, x, y2)

        # app.find_element_by_id('com.ss.android.auto:id/a5i').click()    # 返回上一页
        # app.find_element_by_id('com.ss.android.auto:id/f').click()
        for i in range(2):
            app.back()      # 返回两次，回到选车页面

    def test2_carSearch(self):
        app = self.app

        # for i in range(5):
        #     car = app.find_elements_by_id('com.ss.android.auto:id/brs')    # 选择选车目录
        #     print(car)
        #     if len(car) > 0:
        #         car[1].send_keys()
        #         break
        app.find_elements_by_id('com.ss.android.auto:id/brs')[1].click()    # 选择选车页面
        app.find_element_by_id('com.ss.android.auto:id/ata').click()    # 在搜索框传入值
        app.find_element_by_id('com.ss.android.auto:id/pl').send_keys('宝马')     # 输入宝马
        app.press_keycode(66)         # press_keycode()调用 键盘方法，传入键值，66为回车键，具体查看config/cofing_txt文件
        app.find_element_by_android_uiautomator("new UiSelector().textContains(\"查看更多\")").click()  # 选择查看更多
        app.find_elements_by_android_uiautomator('new UiSelector().text(\"SUV\")')[0].click()
        app.find_elements_by_class_name('android.widget.RelativeLayout')[3].click()     # 选择排行第一的

        # 向上滑动
        size = app.get_window_size()        # 获取窗口大小
        width = size['width']               # 获取宽
        height = size['height']             # 获取长
        for i in range(4):
            x = width * 0.5
            y1 = height * 0.9
            y2 = height * 0.2

            app.swipe(x, y1, x, y2)             # swipe()滑动页面方法，传入起点终点坐标

        # app.find_element_by_id('com.ss.android.auto:id/a5i').click()    # 返回上一页
        # app.find_element_by_id('com.ss.android.auto:id/f').click()     # 返回上一页
        # app.find_element_by_id('com.ss.android.auto:id/yp').click()     # 选择取消，返回搜索页
        # app.find_element_by_id('com.ss.android.auto:id/yp').click()     # 选择取消，返回选车页面
        for i in range(4):
            app.back()          # 返回4次，回到选车页面

    """微信app相关业务"""
    def test10_xiaoePay(self):

        app = self.app
        app.find_elements_by_id('com.tencent.mm:id/rq')[3].click()  # 选择我的
        app.find_elements_by_id('com.tencent.mm:id/d9u')[1].click()     # 选择收藏

        # accessibility_id()定位方式，根据标签的content-desc值定位，括号传入content-desc的值
        app.find_element_by_accessibility_id('搜索').click()       # 选择搜索
        app.find_element_by_id('com.tencent.mm:id/brh').send_keys('灰壮')     # 输入搜索内容
        searct = app.find_element_by_id('com.tencent.mm:id/brh')
        print(searct.text, '1')         # 获取不到文本
        print(searct.get_attribute('name'), '2')    # 获取不到文本
        app.press_keycode(66)       # 输入回车键
        app.find_element_by_id('com.tencent.mm:id/bb').click()      # 进入灰壮

        sleep(5)
        # print(app.current_context)    # 获取当前窗口
        # contexts = app.contexts      # 获取所有窗口
        # print(contexts)
        # app.switch_to.context(contexts[1])    # 切换webview窗口，目前报错，也没用上
        # print(app.current_context)
        app.find_element_by_accessibility_id('更多').click()      # 点击。。。
        app.find_element_by_android_uiautomator('new UiSelector().text(\"发送给朋友\")').click()  # 选择发送给朋友
        app.find_element_by_id('com.tencent.mm:id/b98').send_keys('叨叨')     # 搜索微信昵称‘叨叨’
        app.press_keycode(66)       # 回车
        app.find_elements_by_id('com.tencent.mm:id/de9')[0].click()  # 选择叨叨
        app.find_element_by_id('com.tencent.mm:id/b00').click()     # 点击发送

    def test11_tiaos(self):
        app = self.app
        app.find_elements_by_id('com.tencent.mm:id/rq')[3].click()  # 选择我的
        app.find_elements_by_id('com.tencent.mm:id/d9u')[1].click()     # 选择收藏

        # accessibility_id()定位方式，根据标签的content-desc值定位，括号传入content-desc的值
        app.find_element_by_accessibility_id('搜索').click()       # 选择搜索
        searct = app.find_element_by_xpath('//android.widget.LinearLayout[@resource-id="com.tencent.mm:id/c1"]/'
                                           'android.widget.LinearLayout[0]')
        print(searct.text, '1')         # 获取不到文本
        searct.send_keys('123')
        print(searct.text, '2')    # 获取不到文本

    def test12_appAndsele(self):

        app = self.app
        app.find_elements_by_id('com.tencent.mm:id/rq')[3].click()  # 选择我的
        app.find_elements_by_id('com.tencent.mm:id/d9u')[1].click()  # 选择收藏

        # accessibility_id()定位方式，根据标签的content-desc值定位，括号传入content-desc的值
        app.find_element_by_accessibility_id('搜索').click()  # 选择搜索
        app.find_element_by_id('com.tencent.mm:id/brh').send_keys('国学云平台')  # 输入搜索内容
        app.find_element_by_id('com.tencent.mm:id/bb').click()
        print(app.current_context)
        contexts = app.contexts
        sleep(3)
        print(app.current_context, contexts, contexts[1])
        app._switch_to.context(contexts[1])     # 切换到webview窗口
        # print(app.page_source)
        # app.execute(MobileCommand.SWITCH_TO_CONTEXT, {'name': contexts[1]})
        print('启动成功')
        print(app.current_context)
        app.find_element_by_xpath('//div[@class="btnlist"]/a[1]/div').click()   # 选择上传图片
        sleep(8)
        print(app.contexts)
        app.find_element_by_id('chooseImage').click()           # 选择添加照片
        app._switch_to.context(contexts[0])     # 切换回到android窗口
        print(app.context)
        app.background_app(2)
        print(app.page_source)
        print(app.find_elements_by_id('com.tencent.mm:id/bpy'))
        app.find_elements_by_id('com.tencent.mm:id/bpy')[2].click()     # 选择第3张照片
        sleep(3)
        app.find_element_by_id('com.tencent.mm:id/ki').click()  # 确认
        app._switch_to.context(contexts[1])
        print(app.context)
        app.background_app(2)
        app.find_element_by_id('chooseImage').click()  # 选择添加照片
        app._switch_to.context(contexts[0])
        app.background_app(2)
        app.find_elements_by_id('com.tencent.mm:id/bpy')[2].click()     # 选择第3张照片
        sleep(3)
        app.find_element_by_id('com.tencent.mm:id/ki').click()  # 确认

    def test14_lolSele(self):

        app = self.app
        try:
            update = app.find_element_by_id('com.tencent.tgp:id/tv_negative')
            update.click()
        except:
            pass
        sleep(2)
        print(app.contexts)
        # app.find_element_by_xpath('//android.widget.FrameLayout[@resource-id="com.tencent.tgp:id/tabBarView"]/'
        #                           'android.widget.LinearLayout/android.widget.LinearLayout[3]').click()
        app.find_element_by_android_uiautomator('new UiSelector().text(\"游戏\")').click()
        app.find_element_by_android_uiautomator('new UiSelector().text(\"三国杀\")').click()
        print(app.contexts)
        size = app.get_window_size()
        width = size['width']
        height = size['height']

        x = width * 0.5
        y1 = height * 0.8
        y2 = height * 0.2

        for i in range(2):
            app.swipe(x, y1, x, y2)
        print(app.contexts)
        # app.find_element_by_android_uiautomator('new UiSelector().text(\"游戏介绍\")').click()
        # app.find_element_by_xpath('//android.view.View[@resource-id="app"]/android.view.View[3]').click()
        app.tap([0, 1305], [1080, 1668])
        sleep(5)

    def test15_nubyliu(self):

        app = self.app
        print(app.context)
        contexts = app.contexts
        print(app.contexts)
        app.find_element_by_id('cn.nubia.browser:id/positiveButton').click()
        app.find_element_by_id('cn.nubia.browser:id/item_content_lay').click()
        app._switch_to.context(contexts[1])
        app.background_app(2)
        print(app.find_elements_by_xpath('//div[@class="sub-img"][1]'))
        app.find_elements_by_xpath('//div[@class="sub-img"][1]')[0].click()

    """收集e海通财app报错"""
    def test16_renlianErron(self):

        # adb日志命令
        Adb = {}
        Adb['Clear'] = 'adb -s c09714bd logcat -c -b main -b events -b radio -b system'  # 清除设备c09714bd的缓存日志命令
        Adb['Crash'] = 'adb -s c09714bd logcat -v time -s AndroidRuntime:E'  # 采集运行崩溃日志命令
        Adb['Crash2'] = 'adb -s c09714bd logcat -v time -s AndroidRuntime:E | find "com.android.haitong"'  # 采集运行崩溃日志命令
        Adb['Applog'] = 'adb -s c09714bd logcat -v time *:V | find "adb -s c09714bd logcat -v time *:V |' \
                        ' find "com.android.haitong"'  # 采集e海通财app运行日志

        subprocess.call(Adb['Clear'])       # 清除设备缓存日志
        '''采集崩溃日志'''
        now = time.strftime('%Y-%m-%d', time.localtime())  # 获取当前时间
        file_name = '../report/' + now + 'appLog.log'  # 文件名称加上当前时间
        logcat_file = open(file_name, 'w')  # 写入日志
        Poplog = subprocess.Popen(Adb['Applog'], stdout=logcat_file, stderr=subprocess.PIPE)  # 读取日志并输出

        app = self.app
        # app.find_element_by_id('com.pumpkinstudy.kind:id/login_phone_edit').send_keys('15779582092')
        # app.find_element_by_id('com.pumpkinstudy.kind:id/login_getcode_btn').click()'
        app.find_element_by_android_uiautomator('new UiSelector().text(\"行情\")').click()
        app.find_element_by_android_uiautomator('new UiSelector().text(\"选股\")').click()
        app.find_element_by_id('com.android.haitong:id/item_tv_customchoosestock').click()
        app.find_element_by_android_uiautomator('new UiSelector().text(\"每股净资产\")').click()
        sleep(2)
        app.find_element_by_android_uiautomator('new UiSelector().text(\"大于0\")').click()
        app.find_element_by_id('com.android.haitong:id/item_tv_commit').click()
        app.find_element_by_id('com.android.haitong:id/item_tv_result').click()
        app.find_element_by_id('com.android.haitong:id/item_tv_addoptional').click()
        sleep(5)
        app.find_element_by_id('com.android.haitong:id/icsaddoptional_footerarea').click()

        sleep(60)
        logcat_file.close()  # 关闭文件
        Poplog.terminate()  # 停止采集日志

    def test_info_appLog(self):

        import psutil

        appPackages = 'com.yonghui.freshdelivery'
        Adb = {}
        Adb['getPid'] = 'adb shell ps | findstr ' + appPackages     # 查询app的进程号
        Adb['test'] = 'adb shell dumpsys cpuinfo | findstr ' + appPackages
        Adb['Applog'] = 'adb logcat  -v time *:E | find "com.yonghui.freshdelivery"'  # 采集e海通财app运行日志

        sub = os.popen(Adb['getPid'])   # 执行adb命令， 结果返回为str类型
        list = []
        for i in sub.readline().split(' '):
            if i != '':
                list.append(i.replace('\n', ''))    # 去除空格和换行符，并存入list，pid为list[1]
        sub.close()

        Adb['Pidlog'] = 'adb logcat -v time *:E | findstr ' + list[1]   # 获取进程的日志
        now = time.strftime('%Y-%m-%d', time.localtime())  # 获取当前时间
        file_name = '../report/' + now + 'appLog.log'  # 文件名称加上当前时间
        logcat_file = open(file_name, 'w')  # 创建日志文件
        Poplog = subprocess.Popen(Adb['Pidlog'], start_new_session=True, stdout=logcat_file, stderr=subprocess.PIPE)  # 读取日志并输出

        sleep(5)
        Poplog.terminate()
        Poplog.kill()
        logcat_file.close()


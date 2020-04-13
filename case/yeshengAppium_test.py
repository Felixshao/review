from appium import webdriver


desired_caps = {}
desired_caps['appium_url'] = 'http://localhost:4723/wd/hub'  # appium服务路径
desired_caps['platformName'] = 'Android'  # 自动化设备的平台
desired_caps['platformVersion'] = '9'  # 需要连接的设备版本号
desired_caps['deviceName'] = 'c09714bd'  # 连接的设备名称
# desired_caps['app'] = r'F:\study\study2_appnium\file\toutiao.apk'  # 测试包地址，在设备上自动安装
desired_caps['appPackage'] = 'io.manong.developerdaily'  # 测试包的包名
desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity'  # 启动时进入的Activity
# desired_caps['aotumationName'] = 'Appium'
# desired_caps['autoAcceptAlerts'] = True  # 默认app接受手机所有权限
desired_caps['noReset'] = True  # 不需要再次安装软件
desired_caps['noSign'] = True  # 不重新签名apk
desired_caps['unicodeKeyboard'] = True  # 支持可输入中文
desired_caps['resetKeyboard'] = True  # 重置键盘
desired_caps['newCommandTimeOut'] = '20'  # 没有新命令，10s后退出appium

desired_caps1 = {
            'appium_url': 'http://localhost:4723/wd/hub',   # appium服务器地址
            'platformName': 'Android',                      # 设备操作系统
            'platformVersion': '9',                         # 设备系统版本
            'deviceName': 'c09714bd',                       # 远程连接的设备名称
            'appPackage': 'io.manong.developerdaily',            # 启动的app包名
            'appActivity': 'io.toutiao.android.ui.activity.LaunchActivity',      # app首个activity
            'noReset': True,                                # 启动时不重置（清除）app原有数据
            'noSign': True,                                 # 跳过对应用的签名
            'unicodeKeyboard': True,                        # 使用Unicode输入法
            'resetKeyboard': True,                          # 结束后恢复默认输入法
            'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'},    # 需要切换到webview时加入此配置，value值为webview的context
            'newCommandTimeout': 30,  # 超过30s无下个命令，退出
        }


if __name__ == '__main__':
    print('启动')
    start = webdriver.Remote(desired_caps1['appium_url'], desired_caps1)
    print('结束')
    start.quit()
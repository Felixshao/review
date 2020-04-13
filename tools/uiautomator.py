import os

def uiautomator():
    get_app_uix = 'adb shell uiautomator dump /sdcard/app.uix'
    shell = "echo \"Hello World\""

    uix = os.popen(get_app_uix).read()



    print('uix:', uix)
    print('shell:', shell)


if __name__ == '__main__':

    uiautomator()
import win32api


def open_pc_appium():
    appium_path = 'C:\Program Files (x86)\Appium\Appium.exe'

    win32api.ShellExecute(0, 'open', appium_path, '', '', 1)


if __name__ == '__main__':

    open_pc_appium()
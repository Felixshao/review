import sys
import os


project = 'D:\\study\\python\\review\\DailyWork'
sys.path.append(os.getcwd().split(project)[0]+project)

import random
import time
import unittest
import requests
import warnings
import json         # json库，用来转换json数据
import chardet      # 查看字符编码
from time import sleep
from selenium import webdriver
from public import public
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class sele_case(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        warnings.filterwarnings('ignore')       # 忽略警告

        cls.md = webdriver.Chrome()                # 打开Chrome浏览器
        cls.md.maximize_window()                    # 最大化窗口
        cls.md.implicitly_wait(8)                   # 隐型等待8s
        wait = WebDriverWait(cls.md, 8)            # 显示等待
        pass

    @classmethod
    def tearDownClass(cls):
        sleep(10)
        # cls.md.quit()                             # 结束后关闭浏览器
        pass

    """哔哩哔哩搜索"""
    def test1_bibiSearch(self):
        md = self.md
        md.get('https://www.bilibili.com/')  # 打开bibi网站
        md.find_element_by_xpath('//form[@class="searchform"]/input').send_keys(u'一拳超人')       # 选择搜索框并输入
        md.find_element_by_xpath('//button[@class="search-submit"]').click()                       # 点击搜索
        handle_alls = md.window_handles                      # 此处会切换新窗口，获取所有句柄用来切换操作窗口
        md.switch_to.window(handle_alls[1])                 # 因弹出新窗口，切换句柄，到新窗口运行代码
        md.find_element_by_xpath('//div[@class="filter-wrap"]/ul[1]/li[3]/a').click()      # 筛选最新发布
        md.find_element_by_xpath('//ul[@class="filter-type clearfix duration"]/li[3]/a').click()   # 筛选10-30分钟
        md.find_element_by_xpath('//ul[@class="filter-type clearfix tids_1"]/li[2]/a').click()     # 筛选动画
        md.find_element_by_xpath('//ul[@class="clearfix"]/li[5]/a').click()                        # 选择综合
        md.find_element_by_xpath('//ul[@class="video-list clearfix"]/li[1]/a').click()             # 选择第一个
        handle_alls = md.window_handles
        md.switch_to.window(handle_alls[2])             # 弹出新窗口，切换句柄，到新窗口运行代码
        md.find_element_by_xpath('//span[@class="bilibili-player-iconfont bilibili-player-iconfont-start"]').click()  # 开始播放

    """csdn写入攻略"""
    def test5_csdnWrite(self):
        md = self.md
        md.get('https://www.csdn.net/')     # 进入csdn页面
        print(md.get_cookies())

        login1 = {'name': 'dc_session_id', 'value': '10_1568182060851.686596'}
        login2 = {'name': 'UserToken', 'value': 'ced39d98c6834d408cdc98ba0c6a68d0'}
        login3 = {'name': 'UserInfo', 'value': 'ced39d98c6834d408cdc98ba0c6a68d0'}
        login4 = {'name': 'announcement', 'value': '%257B%2522isLogin%2522%253Atrue%252C%2522announcementUrl%2522%253A%'
                                                   '2522https%253A%252F%252Fblogdev.blog.csdn.net%252Farticle%252Fdetai'
                                                   'ls%252F102605809%2522%252C%2522announcementCount%2522%253A1%252C%25'
                                                   '22announcementExpire%2522%253A262915060%257D'}
        login5 = {'name': 'UN', 'value': 'felixshao123'}
        login6 = {'name': 'UserName', 'value': 'felixshao123'}
        login7 = {'name': 'smidV2', 'value': '201910091748514891b63ab40baf0f74300f501efad836000079feedeb41840'}
        login8 = {'name': 'uuid_tt_dd', 'value': '10_9895254410-1568182060851-636861'}
        login9 = {'name': '__gads', 'value': 'Test'}
        login10 = {'name': 'dc_tos', 'value': 'pzs8rm'}
        login11 = {'name': 'p_uid', 'value': 'U000000'}
        login12 = {'name': 'SESSION', 'value': '11bcf7a1-4f13-4d57-97f0-aeeb56c1f1fd'}
        login13 = {'name': 'AU', 'value': '292'}
        login14 = {'name': 'BT', 'value': '1571758674413'}
        login15 = {'name': 'Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac', 'value': 'Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac!'
                                                                              '5744*1*felixshao123!6525*1*10_9895254410'
                                                                              '-1568182060851-636861'}
        login16 = {'name': 'Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac', 'value': '1571760380'}
        login17 = {'name': 'Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac', 'value': '1571752631,1571752641,1571752661,'
                                                                               '1571752974'}
        md.add_cookie(login1)
        md.add_cookie(login2)
        md.add_cookie(login3)
        md.add_cookie(login4)
        md.add_cookie(login5)
        md.add_cookie(login6)
        md.add_cookie(login7)
        md.add_cookie(login8)
        md.add_cookie(login9)
        md.add_cookie(login10)
        md.add_cookie(login11)
        md.add_cookie(login12)
        md.add_cookie(login13)
        md.add_cookie(login14)
        md.add_cookie(login15)
        md.add_cookie(login16)
        md.add_cookie(login17)
        sleep(2)
        md.refresh()

        print(md.get_cookies())

        # home_handle = md.current_window_handle  # 获取当前窗口
        # md.find_element_by_xpath('//li[@class="write-bolg-btn"]').click()   # 点击写博客
        # handle_all = md.window_handles  # 获取所有窗口
        # for handle in handle_all:
        #     if handle != home_handle:
        #         md.switch_to.window(handle)     # 焦点切换到新的窗口md
        # login_handle = md.current_window_handle     # 切换后，获取当前窗口
        # public.WeddriverWait_Textclick(md, '账号登录')  # 调用WeddriverWait_click方法
        # md.find_element_by_name('all').send_keys('18598270580')     # 输入手机号
        # md.find_element_by_id('password-number').send_keys('13691916244shaos')  # 输入密码
        # public.WeddriverWait_Xpathclick(md, '//button[@class="btn btn-primary"]')   # 点击登录

        # ActionChains(md).perform()

        # md.execute_script("document.getElementById('nc_1_n1z').style.left='260px'")
        # md.find_element_by_xpath('//div[@class="middle-hand"]/button').click()
        # print(md.find_element_by_class_name('editor').text)

    """boos"""
    def test7_boosCookies(self):

        md = self.md
        md.get('https://login.zhipin.com/?ka=header-login')

        cookies = {
            'domain': 'www.zhipin.com',
            'name': '_bl_uid',
            'value': 'kIk7509g4zwmnCiCLo81g4aea69y'
        }
        cookies2 = {
            'domain': 'www.zhipin.com',
            'name': '_uab_collina',
            'value': '156756294905989667471906'
        }
        cookies3 = {
            'domain': '.zhipin.com',
            'name': '__zp_stoken__',
            'value': '0149tWJgflsY%2Fz%2FjLxA1DVizEGbuE8FC7vev%2BMwjs1SPICHrFMVtCQ338Hji'
                     '0WdbpwSu3Z1RHJF9mNusPYBID%2FLXPQ%3D%3D'
        }
        #             'name1': '_uab_collina', 'value1': '156756294905989667471906',
        #             'name2': 'wt', 'value2': 'NPVFvkMZ2hcIAf3s',
        #             'name3': 't', 'value3': 'NPVFvkMZ2hcIAf3s',
        #             'name5': '__l', 'value5': 'l=%2Fwww.zhipin.com%2F&r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DdJdoCgYpbkO5'
        #                                       'qj6XoEtM3t8mrbB7ERY01jV0PBuwaBjngEU3l6lBXDr7F3-hOhhL%26wd%3D%26eqid%3Dafaff4ea00'
        #                                       '0195cb000000065db0170d&friend_source=0&friend_source=0',
        #             'name6': '__zp_stoken__', 'value6': '0149tWJgflsY%2Fz%2FjLxA1DVizEKtec%2BJIqAPfZ8Fa9hA4lngDoLgiD1dlEqO2bSLB'
        #                                                 '81EvR5rIw35YIbNyAmIl2ifqDg%3D%3D',

        # login1 = {'name': '_uab_collina', 'value': '156756294905989667471906',
        #           }
        # login2 = {'name': '_bl_uid', 'value': 'kIk7509g4zwmnCiCLo81g4aea69y'
        #           }
        login3 = {'name': '__zp_stoken__', 'value': '0149tWJgflsY%2Fz%2FjLxA1DVizEKtec%2BJIqAPfZ8Fa9hA4lngDoLgiD1dlEqO'
                                                    '2bSLB81EvR5rIw35YIbNyAmIl2ifqDg%3D%3D'
                  }
        # md.add_cookie(login1)
        # md.add_cookie(login2)
        # md.add_cookie(login3)
        # md.add_cookie(cookies)
        # md.add_cookie(cookies2)
        # md.add_cookie(cookies3)
        sleep(30)
        # md.refresh()
        print(md.get_cookies())
        # token = md.execute_script('window.localStorage.getItem("token")')
        # print(token)

    """加入cookies跳过登录"""
    def test8_xiaoeCookies(self):

        md = self.md
        md.get('https://admin.xiaoe-tech.com/index')
        cookies = {
            'name': 'b_user_token', 'value': 'token_5db01825e32d62o52okBBhue0I0pEs5Qq',
            'name2': 'laravel_session', 'value2': 'eyJpdiI6IjhzS2lobjZNUUNHdFlsY05zVktYaHc9PSIsInZhbHVlIjoid25LeFd'
                                                'xS2phd0syWkNqaERrV04xK08rQ21OdGM4QjlPQmp5ZmVLSFc3dGJFVUZQYmpRYk'
                                                'psd3dKTmh6MVlpU2RoYmxiVnQ2MVhPbjVpRUNkZEM5cGc9PSIsIm1hYyI6Ijc0YT'
                                                'djYzBhZjc0Nzg5OWIwNGY2ZjY1ZmE1ZDkxMTA3ZDQ2NmVmZTRhM2ZmYmNmODNhMT'
                                                'NhY2FlYTBhMjMxNDUifQ%3D%3D'
        }
        md.add_cookie(cookies)
        # md.add_cookie(login2)
        sleep(2)
        md.refresh()

    """lol官网比赛直播"""
    def test8_lolGame(self):

        md = self.md
        md.get('https://lol.qq.com/act/a20190920worlds/index.shtml?e_code=491407&idataid=278057')
        home_handle = md.current_window_handle
        md.find_element_by_link_text('直击2019全球总决赛').click()
        all_handle = md.window_handles
        for handle in all_handle:
            if handle != home_handle:
                md.switch_to.window(handle)

        md.execute_script('window.scrollBy(0, 1100)')    # 向下滚动500px
        player = md.find_element_by_class_name('txp_shadow')    # 找到播放器位子

        ActionChains(md).move_to_element(player).perform()  # 鼠标悬浮在播放器中
        # full_screen = md.find_element_by_class_name('txp_btn txp_btn_fullscreen')     # 全屏按钮

        # 显示等待全屏元素出现并定位，返回一个元素
        # 1.引入WebDriverWait()显示等待方法，传参：driver和等待时间，未找到默认每0.5秒轮询一次，也可加入自定义轮询时间，
        # 配合until()方法加入等待条件，找到返回元素，未找到报错输出message
        # 2.引入EC(expected_conditions)，使用presence_of_element_located方法查找元素是否在页面中
        # 3.引入By，通过制定方式查找元素
        ele = WebDriverWait(md, 5).until(EC.presence_of_element_located
                                         ((By.XPATH, '//txpdiv[@class="txp_right_controls"]/txpdiv[5]')), message="")

        ele.click()         # 点击全屏

    """lol官网查看竞猜记录"""
    def test9_lolQuiz(self):
        md = self.md

        md.get('https://lol.qq.com/main.shtml')     # 进入官网
        home_handle = md.current_window_handle

        md.execute_script('window.scrollBy(0, 200)')       # 往下滑动500px
        sleep(2)
        quiz9 = md.find_element_by_xpath('//div[@id="promoTitleList"]/span[4]')     # 找到s9竞猜导航栏
        ActionChains(md).move_to_element(quiz9).perform()       # 悬浮鼠标
        md.find_element_by_xpath('//ul[@class="promo-img-list"]/li[4]/a').click()   # 选择s9竞猜有奖
        all_handles = md.window_handles
        for handle in all_handles:
            if handle != home_handle:
                md.switch_to.window(handle)     # 切换新窗口句柄

        md.find_element_by_id('ptLoginBtn').click()     # 选择登录
        md.switch_to.frame('loginIframe')   # 切换到iframe窗口
        md.find_element_by_xpath('//div[@class="bottom hide"]/a[1]').click()    # 选择账号密码登录
        md.find_element_by_id('u').send_keys('2310563268')       # 输入账号
        md.find_element_by_id('p').send_keys('13691916244shaos')     # 输入密码
        md.find_element_by_id('login_button').click()       # 登录
        # md.switch_to.default_content()  # 退出iframe窗口
        sleep(2)
        md.execute_script('window.scrollBy(0, 1100)')   # 往下滑动1100px
        md.find_element_by_xpath('//div[@class="btn-box"]/a[2]').click()    # 查看竞猜记录
        md.find_element_by_xpath('//div[@class="pop3-tox"]/a').click()      # 查看积分榜

    """印象笔记官网，创建一个笔记本"""
    def test10_notebook(self):

        md = self.md
        md.get('https://app.yinxiang.com/Login.action')
        md.find_element_by_id('username').send_keys('18598270580')  # 输入手机号
        md.find_element_by_id('loginButton').click()       # 点击继续

        # element_to_be_clickable()方法，判断元素是否可操作
        password = WebDriverWait(md, 5).until(EC.element_to_be_clickable((By.ID, 'password')), message="元素未找到或不可操作")
        password.send_keys('13691916244shaos')
        md.find_element_by_id('loginButton').click()    # 点击登录
        cookies = md.get_cookies()
        print(cookies)
        md.find_element_by_id('gwt-debug-Sidebar-notebooksButton').click()      # 选择笔记本

        # 创建笔记本,presence_of_element_located()判断元素是否出现
        create_notebook = WebDriverWait(md, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'GM2GFRGCCXB')), message='未找到元素')
        # print(create_notebook.is_enabled())   # is_enabled()判断元素是否可操作，返回bool值
        sleep(2)
        create_notebook.click()
        md.find_element_by_class_name('GM2GFRGCNDC').send_keys('每日自动化笔记')   # 写入笔记本标题

        # 点击创建
        create = WebDriverWait(md, 5).until(EC.element_to_be_clickable
                                            ((By.ID, 'gwt-debug-CreateNotebookDialog-confirm')), message='元素未找到或不可操作')
        create.click()

        # while 1:
        #     erron = md.find_element_by_class_name('gwt-InlineLabel').text
        #     if erron == '所输入笔记本名称已存在。请换一个名称。':
        #         num = random.randint(0, 50)
        #         md.find_element_by_class_name('GM2GFRGCNDC').send_keys('每日自动化笔记' + num)  # 写入笔记本标题
        #
        #         # 点击创建
        #         create = WebDriverWait(md, 5).until(EC.element_to_be_clickable
        #                                             ((By.ID, 'gwt-debug-CreateNotebookDialog-confirm')),
        #                                             message='元素未找到或不可操作')
        #         create.click()
        #     else:
        #         break

        # 使用js修改元素为可见
        WebDriverWait(md, 5). \
            until(EC.presence_of_element_located((By.ID, 'gwt-debug-NotebookHeader-name')), message='元素未找到')

        js = "document.getElementById('gwt-debug-NotebookHeader-name').style.display='block'"
        md.execute_script(js)

        # 获取笔记本标题， visibility_of_element_located()判断元素是否隐藏
        notebook_title = WebDriverWait(md, 5).\
            until(EC.visibility_of_element_located((By.ID, 'gwt-debug-NotebookHeader-name')), message='元素未找到或隐藏')
        print(notebook_title.is_displayed())  # is_displayed()查看标签是否隐藏
        print('笔记本标题:', notebook_title.text)
        self.assertEqual(notebook_title.text, '每日自动化笔记', msg='错误，标题不一致，创建失败')

    """写入笔记：第一天"""
    def test11_notes1(self):

        md = self.md
        md = self.md
        md.get('https://app.yinxiang.com/Login.action')
        md.find_element_by_id('username').send_keys('18598270580')  # 输入手机号
        md.find_element_by_id('loginButton').click()  # 点击继续

        # element_to_be_clickable()方法，判断元素是否可操作
        password = WebDriverWait(md, 5).until(EC.element_to_be_clickable((By.ID, 'password')), message="元素未找到或不可操作")
        password.send_keys('13691916244shaos')
        md.find_element_by_id('loginButton').click()  # 点击登录
        md.find_element_by_id('gwt-debug-Sidebar-notebooksButton').click()  # 选择笔记本
        md.find_element_by_id('gwt-debug-NotebooksDrawer-drawerFilter-textBox').send_keys('每日自动化笔记')
        sleep(2)
        md.find_element_by_class_name('GM2GFRGCPWB').click()    # 选择笔记本
        md.refresh()
        md.find_element_by_id('gwt-debug-Sidebar-newNoteButton-container').click()  # 点击新建笔记
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())       # 格式或获取当前时间
        md.find_element_by_id('gwt-debug-NoteTitleView-textBox').send_keys(create_time)  # 写入笔记标题
        md.switch_to.frame('RichTextArea-entinymce')     # 切换进入笔记窗口
        md.find_element_by_id('tinymce').send_keys('第一天：开始记录笔记！')
        md.switch_to.default_content()  # 退出ifrema窗口
        sleep(2)
        md.find_element_by_id('gwt-debug-NoteAttributes-doneButton').click()    # 完成

    """写入笔记：第二天"""
    def test11_notes2(self):

        md = self.md
        md.get('https://app.yinxiang.com/Login.action')
        md.find_element_by_id('username').send_keys('18598270580')  # 输入手机号
        md.find_element_by_id('loginButton').click()  # 点击继续

        # element_to_be_clickable()方法，判断元素是否可操作
        password = WebDriverWait(md, 5).until(EC.element_to_be_clickable((By.ID, 'password')), message="元素未找到或不可操作")
        password.send_keys('13691916244shaos')
        md.find_element_by_id('loginButton').click()  # 点击登录
        md.find_element_by_id('gwt-debug-Sidebar-notebooksButton').click()  # 选择笔记本
        md.find_element_by_id('gwt-debug-NotebooksDrawer-drawerFilter-textBox').send_keys('每日自动化笔记')
        sleep(2)
        md.find_element_by_class_name('GM2GFRGCPWB').click()    # 选择笔记本
        md.refresh()
        md.find_element_by_id('gwt-debug-Sidebar-newNoteButton-container').click()  # 点击新建笔记
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())       # 格式或获取当前时间
        md.find_element_by_id('gwt-debug-NoteTitleView-textBox').send_keys(create_time)  # 写入笔记标题
        md.switch_to.frame('RichTextArea-entinymce')     # 切换进入笔记窗口
        md.find_element_by_id('tinymce').send_keys('第二天：记录笔记！')
        md.switch_to.default_content()  # 退出ifrema窗口
        sleep(2)
        md.find_element_by_id('gwt-debug-NoteAttributes-doneButton').click()    # 完成

    """使用cookies登录"""
    def test11_Cookies_note(self):

        md = self.md
        md.get('https://app.yinxiang.com/Home.action#n=1f8bcf7e-9c00-4115-8eba-66e4c9b7d9af&s=s26&ses=4&sh=2&sds=5&')
        # md.find_element_by_id('username').send_keys('18598270580')  # 输入手机号
        # md.find_element_by_id('loginButton').click()  # 点击继续
        #
        # # element_to_be_clickable()方法，判断元素是否可操作
        # password = WebDriverWait(md, 5).until(EC.element_to_be_clickable((By.ID, 'password')), message="元素未找到或不可操作")
        # password.send_keys('13691916244shaos')
        # md.find_element_by_id('loginButton').click()  # 点击登录
        # cookies = md.get_cookies()
        # print(cookies)
        cookie1 = {'name': 'JSESSIONID', 'value': '363FCBA61799B51CA67673001A796518'}
        cookie2 = {'name': 'cookieTestValue', 'value': '1572691084134'}
        cookie3 = {'name': 'req_sec', 'value': '"U=183d249:P=/:E=16e2bbaac2e:S=dee99d32989bb24de971fc258ccec3ee"'}
        cookie4 = {'name': 'lastAuthentication', 'value': '1572691084285/180f31ec39ce89e82384c95b2607755d'}
        md.add_cookie(cookie1)
        md.add_cookie(cookie2)
        md.add_cookie(cookie3)
        md.add_cookie(cookie4)

        sleep(2)
        md.refresh()

    """cookies登录"""
    def test18_cookiesXiaoe(self):

        md = self.md
        md.quit()
        # # 通过手动加入cookies跳过登录
        # md.get('https://admin.xiaoe-tech.com/index')    # 登录页面地址
        #
        # # 登录依赖的cookies
        # cookie1 = {
        #     'name': 'laravel_session', 'value': 'eyJpdiI6IkZwOUFzNGduXC9SZElpVEI0aWhobW53PT0iLCJ2YWx1ZSI6InRXbzNUbHI'
        #                                         '3SXlLcWhyR1E4UmxqNHRMdFFoVlFJMW9kN1VWbzdMU1wvV1VGRTE5aVhSRkF3K3NpbF'
        #                                         'I5eTdmMExcLzZKdnFjMGptdXE0K3ZoZGVib0lLVUE9PSIsIm1hYyI6IjU3MGY3ZDg0O'
        #                                         'TE2OTRiNjM4Y2RkMmE2MTgzZWMwMzE5OThlODBhODc1MTdlODQxZWMxMjZkZGI4NmM5'
        #                                         'YjMyOGMifQ%3D%3D'
        # }
        # cookie2 = {'name': 'b_user_token', 'value': 'token_5dbfa6c9aa681q9bBMOx7dQQedmmrWM4j'}
        #
        # # add.cookie方法加入cookies
        # md.add_cookie(cookie1)
        # md.add_cookie(cookie2)      # 给当前页面加入cookies，cookies参数需为字典类型，且带有name和value值格式
        # sleep(2)
        #
        # # 刷新页面后，自动进入首页
        # md.refresh()
        #
        # sleep(3)
        #
        # # 获取页面cookies，以列表方式存储
        # cookies1 = md.get_cookies()

        # 获取页面cookies，并已字典方式存储
        # cookies2 = {
        #     'laravel_session': cookies1[2]['value'],
        #     'b_user_token': cookies1[7]['value']
        # }
        """----------------------------------------------------------------------------------------------------"""
        cookies3 = {
            'laravel_session': 'eyJpdiI6IkZwOUFzNGduXC9SZElpVEI0aWhobW53PT0iLCJ2YWx1ZSI6InRXbzNUbHI3SXlLcWhyR1E4Umxq'
                               'NHRMdFFoVlFJMW9kN1VWbzdMU1wvV1VGRTE5aVhSRkF3K3NpbFI5eTdmMExcLzZKdnFjMGptdXE0K3ZoZGVib'
                               '0lLVUE9PSIsIm1hYyI6IjU3MGY3ZDg0OTE2OTRiNjM4Y2RkMmE2MTgzZWMwMzE5OThlODBhODc1MTdlODQxZW'
                               'MxMjZkZGI4NmM5YjMyOGMifQ%3D%3D',
            'b_user_token': 'token_5dbfa6c9aa681q9bBMOx7dQQedmmrWM4j'
        }
        print(cookies3, '\n')

        # 使用获取的cookies来完成接口运行
        url = 'https://admin.xiaoe-tech.com/evaluation_work/exercise/set_exercise_book_system_state'
        json1 = {'is_show_exercise_system': '0'}     # 字典类型参数

        # requests.post请求，cookies的参数传值类型：1.传入字典类型参数；2.以requests.cookies.RequestsCookieJar类型
        # 接口参数传值。1：data方式：dict类型、
        quitbooks = requests.post(url, params=json1, cookies=cookies3, verify=False)
        # cookies4 = quitbooks.cookies    # 获取请求的cookies。，类型为requests.cookies.RequestsCookieJar
        result = json.loads(quitbooks.text)  # 将json格式的str转换为dict
        print(type(result))
        print(quitbooks.status_code)
        # self.assertEqual(0, int(result['code']), msg='erron，响应结果为{}'.format(result["code"]))

        # param2 = {'is_show_exercise_system': '1'}
        # quitbooks2 = requests.post(url, json=param2, cookies=cookies3, verify=False)
        # print(quitbooks2.status_code)
        # print(quitbooks2.text)

    """小鹅打卡用户搜索"""
    def test20_test(self):

        self.md.quit()
        url = 'https://admin.xiaoe-tech.com/punch_card/get_clock_user_list'

        cookies3 = {
            'laravel_session': 'eyJpdiI6IkZwOUFzNGduXC9SZElpVEI0aWhobW53PT0iLCJ2YWx1ZSI6InRXbzNUbHI3SXlLcWhyR1E4Umxq'
                               'NHRMdFFoVlFJMW9kN1VWbzdMU1wvV1VGRTE5aVhSRkF3K3NpbFI5eTdmMExcLzZKdnFjMGptdXE0K3ZoZGVib'
                               '0lLVUE9PSIsIm1hYyI6IjU3MGY3ZDg0OTE2OTRiNjM4Y2RkMmE2MTgzZWMwMzE5OThlODBhODc1MTdlODQxZW'
                               'MxMjZkZGI4NmM5YjMyOGMifQ%3D%3D',
            'b_user_token': 'token_5dbfa6c9aa681q9bBMOx7dQQedmmrWM4j'
        }

        params1 = {'page': '1', 'page_size': '15', 'search_content': '你好'}

        pubch_search = requests.post(url, params=params1, cookies=cookies3, verify=False)
        print(pubch_search.url)     # 获取请求链接
        print(pubch_search.text)    # 获取响应结果，自动编码为字符串类型，有时会出错，可以以content方式获取，再手动编码
        print(pubch_search.content)  # 获取响应结果，为字节字符串类型
        print(pubch_search.cookies)     # 获取cookies，类型为requests.cookies.RequestsCookieJar
        print(pubch_search.headers)     # 获取请求头
        print(pubch_search.apparent_encoding)   # 获取网页编码
        print(pubch_search.history)
        print(pubch_search.status_code)     # 返回响应码
        print(pubch_search.elapsed)         # 获取接口实际响应时间，具体方法查看文档：https://www.cnblogs.com/yoyoketang/p/8035428.html

    """小鹅用户搜索"""
    def test21_test2(self):

        self.md.quit()
        url = 'https://admin.xiaoe-tech.com/new/customerList'

        cookies3 = {
            'laravel_session': 'eyJpdiI6IkZwOUFzNGduXC9SZElpVEI0aWhobW53PT0iLCJ2YWx1ZSI6InRXbzNUbHI3SXlLcWhyR1E4Umxq'
                               'NHRMdFFoVlFJMW9kN1VWbzdMU1wvV1VGRTE5aVhSRkF3K3NpbFI5eTdmMExcLzZKdnFjMGptdXE0K3ZoZGVib'
                               '0lLVUE9PSIsIm1hYyI6IjU3MGY3ZDg0OTE2OTRiNjM4Y2RkMmE2MTgzZWMwMzE5OThlODBhODc1MTdlODQxZW'
                               'MxMjZkZGI4NmM5YjMyOGMifQ%3D%3D',
            'b_user_token': 'token_5dbfa6c9aa681q9bBMOx7dQQedmmrWM4j'
        }

        params1 = {'is_pay': '0', 'search': 'f', 'page': '1', 'ruler': ''}

        user_search = requests.get(url, json=params1, cookies=cookies3, verify=False)
        print(user_search.url)
        print(user_search.text)
        self.md.find_element().is_selected()

    """selenium截图"""
    def test22_screenshot(self):
        md = self.md
        file_name = '..\\file\\one.png'
        md.get("https://www.baidu.com")
        md.save_screenshot(file_name)   # save_screenshot方法，截取图片并命名存入文件夹中
        md.get_screenshot_as_file(file_name)    # get_screenshot_as_file方法，截取图片并命名存入文件夹中





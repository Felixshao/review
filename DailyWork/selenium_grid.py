# _*_ config: utf-8 _*_
# selenium分布式
# selenium_grid.py
import time

from selenium.webdriver import Remote
import multiprocessing as mp


driver = Remote(command_executor='http://169.254.163.156:4445/wd/hub',  # hub的地址
                desired_capabilities={'platform': 'ANY',
                                      'browserName': 'chrome',        # 选择浏览器
                                      'version': '',
                                      'javascriptEnable': True
                                      }
                )

# 节点地址和浏览器
lists = {'http://169.254.163.156:4455/wd/hub': 'chrome',
         'http://169.254.163.156:4466/wd/hub': 'firefox',
         'http://169.254.163.156:4477/wd/hub': 'chrome'
         }


def open_browsr(host, browser):
    """启动指定节点指定浏览器"""
    driver = Remote(command_executor=host, desired_capabilities={'platform': 'ANY',
                                                                     'browserName': browser,
                                                                     'version': '',
                                                                     'javascriptEnabled': True
                                                                     })

    driver.get('https://www.baidu.com/')
    driver.find_element_by_id('kw').send_keys('python')
    driver.find_element_by_id('su').click()
    time.sleep(2)
    driver.quit()


def more_process():
    """多进程通过节点启动不同浏览器"""
    pool = mp.Pool()
    for host, browser in lists.items():

        pool.apply_async(open_browsr, args=(host, browser))
    pool.close()
    pool.join()


if __name__ == '__main__':
    more_process()




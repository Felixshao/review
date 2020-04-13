import sys
import os
import unittest
import yagmail
import time
import multiprocessing as mp
from config.HtmlTestRunner import HTMLTestRunner
from config.BeautifulReport import BeautifulReport
from multiprocessing import Process

path = os.path.split(os.path.abspath(__file__))[0]
project = 'D:\\study\\python\\review\\DailyWork'
sys.path.append(os.getcwd().split(project)[0]+project)
case_patn = 'D:\\study\\python\\review\\testcase'
test_case = ['four10_test.py', 'four11_test.py', 'four12_test.py', 'four13_test.py', 'four14_test.py', 'four15_test.py',
             'four16_test.py', 'four17_test.py', 'four18_test.py', 'four19_test.py', 'four1_test.py', 'four20_test.py',
             'four2_test.py', 'four3_test.py', 'four4_test.py', 'four5_test.py', 'four6_test.py', 'four7_test.py',
             'four8_test.py', 'four9_test.py', 'four_test.py', 'one_test.py', 'three_test.py', 'two_test.py']

def testcase():

    all_files = os.listdir(case_patn)
    file_list = []
    for i in all_files:
        file_list.append(i)
    print(file_list)

def case_suite():
    case_suite = unittest.TestSuite()
    suite_list = []
    for i in range(2):
        suite = unittest.defaultTestLoader.discover(start_dir=case_patn, pattern=test_case[i], top_level_dir=case_patn)
        suite_list.append(suite)
    # return suite_list
    for suite in suite_list:
        case_suite.addTest(suite)
    return case_suite

def run(suite, q, process):
    runny = BeautifulReport(suite, verbosity=2)
    result = runny.report(description='多进程报告', filename='\\report1', log_path=os.path.join(path, 'report'),
                          process=process)
    q.put(result)

def process():
    suites = case_suite()
    pros = []
    results = []
    q = mp.Queue(maxsize=len(test_case))
    for suite in suites:
        pro = Process(target=run, args=(suite, q, True))
        pros.append(pro)
    for pro in pros:
        pro.start()

    for pro in pros:
        pro.join()
        results.append(q.get())
    return results, suites

def pool():
    suites = case_suite()
    pool = mp.Pool()
    results = []
    q = mp.Manager().Queue()
    for suite in suites:
        pool.apply_async(run, args=(suite, q, True))
    pool.close()
    pool.join()
    for i in range(q.qsize()):
        results.append(q.get())
    return results, suites


if __name__ == '__main__':
    results, suites = process()
    dict = {}
    for i in range(len(results)):
        if i == 0:
            dict['testName'] = results[0]['testName']
            dict['beginTime'] = results[0]['beginTime']
            dict['testPass'] = results[i]['testPass']
            dict['testResult'] = results[i]['testResult']
            dict['testAll'] = results[i]['testAll']
            dict['testFail'] = results[i]['testFail']
            dict['testSkip'] = results[i]['testSkip']
            dict['testError'] = results[i]['testError']
        else:
            dict['testPass'] += results[i]['testPass']
            dict['testResult'] += results[i]['testResult']
            dict['testAll'] += results[i]['testAll']
            dict['testFail'] += results[i]['testFail']
            dict['testSkip'] += results[i]['testSkip']
            dict['testError'] += results[i]['testError']
        dict['totalTime'] = results[i]['totalTime']
    result = BeautifulReport(suites)
    result.stop_output(log_path=os.path.join(path, 'report') + '\\', FIELDS=dict)

# if __name__ == '__main__':
#
#     # 创建一个测试套件，unittest.defaultTestLoader.discover()方法，将package包作为套件，传入参数，包名和py文件的名字格式
#     testsuit = unittest.defaultTestLoader.discover('DailyWork', pattern='highTutorial_test.py')
#
#     repolt_file = open('.\\report\\report.html', 'wb')      # 创建一份html测试报告
#     runny = HTMLTestRunner(repolt_file, verbosity=2, title='自动化报告')      # 初始化测试套件的执行器
#     runny.run(testsuit)                    # 执行测试套件
#
#     # 连接发送者邮箱服务器
#     # send_mail = yagmail.SMTP(user='shaoyufei1234@163.com', password='13691916244shaos', host='smtp.163.com')
#     # # time.time()获取当前时间时间戳，loacltime()格式化时间戳为本地时间，strftime()优化格式化版本
#     # current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))   # 获取当前时间并格式化
#     #
#     # # 发送邮件
#     # attachments = ['.\\report\\report.html', '.\\report\\inter_log.txt']
#     # send_mail.send(to='1223725877@qq.com', subject='自动化报告-标题', contents=current_time + '自动化报告-正文',
#     #                attachments=attachments)




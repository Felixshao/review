import threading
import time
import unittest
from DailyWork.highTutorial_test import high_case
from tomorrow import threads
from selenium import webdriver

num = 20
lock = threading.Lock()
thnum = 0
f_flag = 0

# def print_num(n=1):
#     global num
#     lock.acquire()
#     num = num - n
#
#     lock.release()
#     return num


def run():
    for i in range(10000):
        global thnum
        thnum += 1
    global f_flag
    f_flag = 1
    print('run num:', num)


def print_num3():
    while True:
        if f_flag != 0:
            for i in range(10000):
                global thnum
                thnum += 1
            break
    print('print_num3 num:', num)

def thread_create():

    # 创建线程，参数：函数名，参数
    thread1 = threading.Thread(target=run)
    thread2 = threading.Thread(target=print_num3)

     # 运行线程
    thread1.start()
    time.sleep(2)
    thread2.start()
    # 等待线程并结束
    thread1.join()
    thread2.join()


if __name__ == '__main__':
    thread_create()

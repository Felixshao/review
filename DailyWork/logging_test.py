import logging
import os
from logging.handlers import TimedRotatingFileHandler

path = 'D:\\study\\python\\review\\report'

def logger1(log_name=None):
    """
    设置日志级别和格式并写入日志文件中
    params：log_name;名称记录器，为None时返回root
    return log;返回logger对象
    """
    log = logging.getLogger(log_name)
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=os.path.join(path, 'logs.log'),
                        filemode='w'
                        )
    return log

def logger2(log_name=None):
    """
    日志打印在控制台并写入日志文件中
    :param log_name:
    :return:log
    """
    log = logging.getLogger(log_name)
    logging.root.setLevel(logging.WARNING)  # 设置日志级别
    # log.setLevel(logging.DEBUG)
    # 创建一个handler的，用于写入文件
    log_path = os.path.join(path, 'logs2.log')
    fh = logging.FileHandler(log_path)

    # 再创建一个句柄，用于输出到控制台
    ch = logging.StreamHandler()

    # 设置日志格式
    format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(format)     # 文件内日志设置格式
    ch.setFormatter(format)     # 控制台内日志设置格式

    # 设置日志级别
    fh.setLevel('DEBUG')
    ch.setLevel('DEBUG')

    log.addHandler(fh)  # logger对象加入写入文件句柄
    log.addHandler(ch)  # logger对象加入控制台句柄

    log.debug('logger2 debug message')
    # log.info('logger2 info message')
    # log.error('logger2 error message')
    # log.warning('logger2 warning message')
    # log.critical('logger2 critical message')

    return log

def logger3(log_name=None):

    log = logging.getLogger(log_name)
    log.setLevel(logging.DEBUG)

    log_path = os.path.join(path, 'logs3.log')
    # 创建一个句柄，用于写入文件，设置每天创建一个新的日志文件，最多创建5个，超过了新的文件覆盖旧日志文件
    # 参数:(when:S(每秒),M(每分),H(每时),D(每天)), (backupCount:数量，控制日志文件个数， interval:数字，和when参数相乘控制创建新日志文件的时间)
    fh = TimedRotatingFileHandler(log_path, when='D', backupCount=5, encoding='utf-8', interval=1)

    ch = logging.StreamHandler()

    format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    fh.setFormatter(format)
    ch.setFormatter(format)

    log.addHandler(fh)
    log.addHandler(ch)

    return log


if __name__ == '__main__':

    logger2('logging_test_main').info('logger3 error message')

    # flag = True
    #
    # if not flag:
    #     print(1)
    # else:
    #     print(2)

    # print(type(log))
    # log.info('info message')
    # logging.error('error message')
    # logging.warning('warning message')
    # logging.critical('critical message')
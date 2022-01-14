# -*- coding: utf-8 -*-
import datetime
import logging
from logging import handlers


class Logger(object):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }  # 日志级别关系映射

    def __init__(self, filename, level='info', when='D', backCount=3,
                 fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)  # 设置日志格式
        self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别
        sh = logging.StreamHandler()  # 往屏幕上输出
        sh.setFormatter(format_str)  # 设置屏幕上显示的格式
        # 实例化TimedRotatingFileHandler
        # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount,
                                               encoding='utf-8')  # 往文件里写入#指定间隔时间自动生成文件的处理器
        th.setFormatter(format_str)  # 设置文件里写入的格式
        self.logger.addHandler(sh)  # 把对象加到logger里
        self.logger.addHandler(th)


def is_date_valid(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        print("> Incorrect data format, should be YYYY-MM-DD")
        return False
    return True


def get_week_begin(date_text):
    '''
    calculate date of Monday at that week
    :param date_text: str, 'YYYY-MM-DD'
    :return:
    '''
    day = datetime.datetime.strptime(date_text, '%Y-%m-%d')
    return datetime.datetime.strftime(day - datetime.timedelta(day.weekday()), "%Y-%m-%d")


def get_week_end(date_text):
    '''
    calculate date of Sunday at that week
    :param date_text: str, 'YYYY-MM-DD'
    :return:
    '''
    day = datetime.datetime.strptime(date_text, '%Y-%m-%d')
    return datetime.datetime.strftime(day + datetime.timedelta(7 - day.weekday() - 1), "%Y-%m-%d")

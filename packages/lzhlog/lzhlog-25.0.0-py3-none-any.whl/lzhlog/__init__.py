# -*- coding: UTF-8 -*-
# Public package
import os
import time
import logging
import inspect
import colorlog
# Private package
# Internal package


def log(name: str = '',  # log名称
        stream: bool = True,  # 是否输出屏幕
        file: str = None,  # 输出文件
        level: str = 'INFO') -> logging.Logger:  # 等级
    logger = logging.getLogger(name=name)
    logger.handlers.clear()
    logger.setLevel(level)
    handlers = []
    if (stream):
        handler = logging.StreamHandler()
        formatter = colorlog.ColoredFormatter('[%(red)s%(asctime)s%(reset)s][%(blue)s%(name)s%(reset)s][%(log_color)s%(levelname)s%(reset)s]: %(message)s')
        handler.setFormatter(formatter)
        handlers.append(handler)
    if (file is not None):
        if (os.path.dirname(file) != '' and not os.path.exists(os.path.dirname(file))):
            os.makedirs(os.path.dirname(file), exist_ok=True)
        handler = logging.FileHandler(file, 'w+')
        formatter = logging.Formatter('[%(asctime)s][%(name)s][%(levelname)s]: %(message)s')
        handler.setFormatter(formatter)
        handlers.append(handler)
    for handler in handlers:
        handler.setLevel(level)
        logger.addHandler(handler)
    logger.propagate = False
    return logger


def get_class_logger(object, **argv) -> logging.Logger:  # 返回某一个类的自动logger
    return log(name='%s.%s' % (inspect.getmodule(object).__name__, type(object).__qualname__), **argv)


def get_func_logger(func, **argv) -> logging.Logger:  # 返回某一个函数的自动logger
    return log(name='%s.%s' % (inspect.getmodule(func).__name__, func.__qualname__), **argv)


def dec_timer(func):  # 修饰器，返回函数运行时间
    def output_func(*args, **argv):
        time_start = time.perf_counter()
        result = func(*args, **argv)
        time_end = time.perf_counter()
        logger = get_func_logger(func, level='INFO')
        logger.info('time cost: {:.2f}s'.format(time_end - time_start))
        return result
    return output_func

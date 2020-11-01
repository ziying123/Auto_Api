#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Script content introduction
__author__ = 'ziying'
__date__ = '2020/11/1 14:23'
__function__ = ''
"""

import pytest

from tools.logger import logger
from tools.send_mail import send_report


@pytest.fixture(scope="class")
def fix_class_level():
    logger.info('*' * 25 + "类下的用例开始执行" + '*' * 25 + '\n')
    yield
    logger.info('*' * 25 + "类下的用例结束" + '*' * 25)
    send_report()  # 发送邮件


@pytest.fixture(scope='function')
def fix_function_level():
    logger.info('='*17 + "单个函数用例开始执行" + '='*17)
    yield
    logger.info('='*17 + "单个函数用例结束执行" + '='*17 + '\n')


@pytest.fixture(scope='module')
def fix_module_level():
    logger.info('='*17 + "单个模块用例开始执行" + '='*17)
    yield
    logger.info('='*17 + "单个模块用例结束执行" + '='*17 + '\n')


@pytest.fixture(scope='session')
def fix_session_level():
    logger.info('='*17 + "单个会话用例开始执行" + '='*17)
    yield
    logger.info('='*17 + "单个会话用例结束执行" + '='*17 + '\n')


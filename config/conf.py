#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Script content introduction
__author__ = 'ziying'
__date__ = '2020/11/1 14:23'
__function__ = '配置文件'
"""

import os
from configparser import ConfigParser


# 项目目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置文件
INI_PATH = os.path.join(BASE_DIR, 'config', 'config.ini')

# 日志目录
LOG_PATH = os.path.join(BASE_DIR, 'logs')

# 报告目录
REPORT_PATH = os.path.join(BASE_DIR, 'report', 'report.html')

# 用例的路径
CASE_DIR = os.path.join(BASE_DIR, 'TestCase')

# 测试数据的路径
DATA_DIR = os.path.join(BASE_DIR, 'test_data', 'data.xlsx')

# 邮件信息
EMAIL_INFO = {
    'username': 'xxxxxx@qq.com',  # 切换成你自己的地址
    'password': 'xxxxxx',
    'smtp_host': 'smtp.qq.com',
    'smtp_port': 465
}

# 收件人
ADDRESSEE = [
    'xxxxxx@163.com',
]


class MyConfig:
    def __init__(self):

        config = ConfigParser()
        config.read(INI_PATH, 'utf-8')

        # 配置环境，SCE是生成环境, PE是测试环境
        self.environment = config.get("host", "host")
        # 用户名手机号
        self.username = config.get("data", "username")
        # 密码
        self.password = config.get("data", "password")
        # 验证码
        self.auth_code = config.get("data", "auth_code")
        # 错误密码
        self.error_pwd = config.get("data", "error_pwd")
        # 错误五位数密码
        self.five_pwd = config.get("data", "five_pwd")


myconfig = MyConfig()

if __name__ == '__main__':
    print(BASE_DIR)

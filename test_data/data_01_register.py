#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Script content introduction
__author__ = 'ziying'
__date__ = '2020/11/1 14:23'
__function__ = ''
"""

register_data = [
    {'CaseID': 1, 'Title': '用户名为空', 'Data': '{"username": None, "password1": "123456", "password2": "123456"}',
     'check': '{"code": 0, "msg": "所有参数不能为空"}'},
    {'CaseID': 2, 'Title': '密码为空，确认密码不为空', 'Data': '{"username": "python14", "password1": None, "password2": "123456"}',
     'check': '{"code": 0, "msg": "所有参数不能为空"}'},
    {'CaseID': 3, 'Title': '密码不为空，确认密码为空', 'Data': '{"username": "python14", "password1": "123456", "password2": None}',
     'check': '{"code": 0, "msg": "所有参数不能为空"}'},
    {'CaseID': 4, 'Title': '密码和确认密码都为空', 'Data': '{"username": "python14", "password1": None, "password2": None}',
     'check': '{"code": 0, "msg": "所有参数不能为空"}'},
    {'CaseID': 5, 'Title': '用户名、密码和确认密码都为空', 'Data': '{"username": None, "password1": None, "password2": None}',
     'check': '{"code": 0, "msg": "所有参数不能为空"}'},
    {'CaseID': 6, 'Title': '两次密码不一致', 'Data': '{"username": "python14", "password1": "123456", "password2": "123"}',
     'check': '{"code": 0, "msg": "两次密码不一致"}'},
    {'CaseID': 7, 'Title': '账户已存在', 'Data': '{"username": "python26", "password1": "123456", "password2": "123456"}',
     'check': '{"code": 0, "msg": "该账户已存在"}'},
    {'CaseID': 8, 'Title': '密码小于6位', 'Data': '{"username": "python14", "password1": "123", "password2": "123"}',
     'check': '{"code": 0, "msg": "账号和密码必须在6-18位之间"}'},
    {'CaseID': 9, 'Title': '密码大于18位',
     'Data': '{"username": "python14", "password1": "12345612345612345612", "password2": "12345612345612345612"}',
     'check': '{"code": 0, "msg": "账号和密码必须在6-18位之间"}'},
    {'CaseID': 10, 'Title': '账号小于6位', 'Data': '{"username": "pyt", "password1": "123456", "password2": "123456"}',
     'check': '{"code": 0, "msg": "账号和密码必须在6-18位之间"}'},
    {'CaseID': 11, 'Title': '账号大于18位',
     'Data': '{"username": "python14python14123456", "password1": "123456", "password2": "123456"}',
     'check': '{"code": 0, "msg": "账号和密码必须在6-18位之间"}'},
    {'CaseID': 12, 'Title': '注册成功', 'Data': '{"username": "python14", "password1": "123456", "password2": "123456"}',
     'check': '{"code": 1, "msg": "注册成功"}'}
]

data_one = [
    {'CaseID': 1, 'Title': '用户名为空', 'Data': '{"username": None, "password1": "123456", "password2": "123456"}',
     'check': '{"code": 0, "msg": "所有参数不能为空"}'}
]

practise = [("我", "I"), ("你", "you"), ("他", "he")]

# _*_ coding: utf-8 _*_

"""Script content introduction
__author__ = 'ziying'
__date__ = '2020/11/1 15:01'
__function__ = 'xxx'
"""

import requests


class RequestHandler:
    def __init__(self):
        """session管理器"""
        self.session = requests.session()

    def visit(self, method, url, params=None, data=None, json=None, headers=None, **kwargs):
        return self.session.request(method, url, params=params, data=data, json=json, headers=headers, **kwargs)

    def close_session(self):
        """关闭session"""
        self.session.close()


if __name__ == '__main__':
    # 以下是测试代码
    # post请求接口
    url = 'http://127.0.0.1:8000/login/'
    payload = {
        "username": "",
        "password": ""
    }
    req = RequestHandler()
    login_res = req.visit("post", url, json=payload)
    print(login_res.text)

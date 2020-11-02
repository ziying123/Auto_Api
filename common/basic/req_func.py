# _*_ coding: utf-8 _*_

"""Script content introduction
__author__ = 'ziying'
__date__ = '2020/11/1 15:01'
__function__ = 'xxx'
"""

import requests
import json


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

    url = 'http://mp-ttsx-python.itheima.net/user/login'
    url1 = 'https://api.github.com/'

    payload = {
        "username": "",
        "password": ""
    }

    headers = {
        "Content-Type": "application/json; charset=utf-8",
        'Connection': 'keep-alive'
    }

    req = RequestHandler()
    res = req.visit("post", url, data=json.dumps(payload), headers=headers)

    try:
        print(res.status_code, res.reason)
        if res.status_code != 200 or res.reason != "OK":
            raise Exception
        st = res.json()
        print(st)
    except Exception as e:
        print(e)
        raise

    res1 = req.visit("get", url1, headers=headers)

    try:
        print(res1.status_code, res1.reason)
        if res1.status_code == 200 and res1.reason == "OK":
            st = res1.json()
            print(st)
    except Exception as e:
        print(e)
        raise

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Script content introduction
__author__ = 'ziying'
__date__ = '2020/11/1 14:23'
__function__ = ''
"""

import pytest
import os
import json

from common.until.register import register
from common.basic.req_func import RequestHandler
from tools.do_excel import DoExcel
from tools.logger import logger
from config.conf import DATA_DIR

do_excel = DoExcel(DATA_DIR, "register")
TestData = do_excel.get_data()
do_excel.close_file()


@pytest.mark.usefixtures("fix_class_level")
class TestRegister:

    @pytest.mark.usefixtures("fix_function_level")
    @pytest.mark.register
    @pytest.mark.parametrize("case", TestData)  # 读取excel文件中的测试用例
    def test_register(self, case):

        logger.info("开始执行第 {} 条用例：{}！".format(case["CaseID"], case["Title"]))
        logger.info("测试数据：{}".format(eval(case["Data"])))

        # 模擬注冊功能
        # data_res = register(eval(case["Data"])["username"],
        #                        eval(case["Data"])["password1"],
        #                        eval(case["Data"])["password2"])

        logger.info("预期结果为：{}".format(eval(case["check"])))

        # 3、断言：预期结果与实际结果的比对
        try:
            # self.assertEqual(res, eval(case["check"]))
            url = 'http://127.0.0.1:8000/user/login/'
            payload = {
                "username": "xxx",
                "password": "xxxxx"
            }
            req = RequestHandler()
            login_res = req.visit("post", url, data=json.dumps(payload))
            # print(login_res)
            # print(login_res.json())

            ts_res = {
                "code": login_res.status_code,
                "msg": login_res.reason
            }

            # logger.info("实际运行结果为：{}".format(ts_res))
            logger.info("实际运行结果为：{}".format(ts_res))

            # assert 200 == login_res['code']
            # assert login_res['msg'] == '登陸成功'

            assert eval(case["check"]) == login_res
            # assert res == eval(case["check"])
        except AssertionError:
            logger.exception("断言失败，第 {} 用例执行不通过！！".format(case["CaseID"]))
            raise
        else:
            logger.info("断言成功，第 {} 用例执行通过！".format(case["CaseID"]))


if __name__ == '__main__':
    pytest.main(['TestCase/test_01_registe.py', '--alluredir=Outputs/allure'])
    os.system('allure serve Outputs/allure')

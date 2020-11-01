# _*_ coding: utf-8 _*_

"""Script content introduction
__author__ = 'ziying'
__date__ = '2020/11/1 14:47'
__function__ = 'xxx'
"""

import pytest
import os
import json
from common.until.register import register
from tools.do_excel import DoExcel
from tools.logger import logger
from config.conf import DATA_DIR
from common.basic.req_func import RequestHandler

do_excel = DoExcel(DATA_DIR, "register")
TestData = do_excel.get_data()
do_excel.close_file()


@pytest.mark.usefixtures("fix_class_level")
class TestLogin:

    @pytest.mark.usefixtures("fix_function_level")
    def test_register(self):

        # logger.info("测试数据：{}".format(eval(case["Data"])))
        # logger.info("预期结果为：{}".format(eval(case["check"])))
        #
        # logger.info("实际运行结果为：{}".format(res))
        # 3、断言：预期结果与实际结果的比对
        try:
            # assert res == eval(case["check"])
            url = 'http://127.0.0.1:8000/login/'
            payload = {
                "username": "",
                "password": ""
            }
            req = RequestHandler()
            login_res = req.visit("post", url, json=payload)

            print(login_res)

        except AssertionError:
            pass
            # logger.exception("断言失败，第 {} 用例执行不通过！！".format(case["CaseID"]))
            raise
        else:
            # logger.info("断言成功，第 {} 用例执行通过！".format(case["CaseID"]))
            pass


if __name__ == '__main__':
    pytest.main(['TestCase/test_02_login.py', '--alluredir=Outputs/allure'])
    os.system('allure serve Outputs/allure')

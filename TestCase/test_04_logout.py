# _*_ coding: utf-8 _*_

"""Script content introduction
__author__ = 'ziying'
__date__ = '2020/11/1 14:48'
__function__ = 'xxx'
"""


import pytest
import os

from common.basic.req_func import RequestHandler
from tools.do_excel import DoExcel
from tools.logger import logger
from config.conf import DATA_DIR

do_excel = DoExcel(DATA_DIR, "register")
TestData = do_excel.get_data()
do_excel.close_file()


@pytest.mark.usefixtures("fix_class_level")
class TestLogout:

    @pytest.mark.usefixtures("fix_function_level")
    def test_logout(self):

        # logger.info("测试数据：{}".format(eval(case["Data"])))
        # logger.info("预期结果为：{}".format(eval(case["check"])))
        #
        # logger.info("实际运行结果为：{}".format(res))
        # 3、断言：预期结果与实际结果的比对
        try:
            # assert res == eval(case["check"])
            url = 'http://127.0.0.1:8000/user/logout/'
            payload = {
                "username": "xxx",
                "password": "xxxxx"
            }
            req = RequestHandler()
            login_res = req.visit("post", url, json=payload)

            print(login_res)

            assert 200 == login_res['code']
            assert login_res['msg'] == '登陸成功'

        except AssertionError:

            logger.exception("断言失败, 登錄失敗")
            raise
        else:
            logger.info("断言成功，登錄成功")


if __name__ == '__main__':
    pytest.main(['TestCase/test_04_logout.py', '--alluredir=Outputs/allure'])
    os.system('allure serve Outputs/allure')

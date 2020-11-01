# _*_ coding: utf-8 _*_

"""Script content introduction
__author__ = 'ziying'
__date__ = '2020/11/1 14:47'
__function__ = 'xxx'
"""

import pytest
import os
from common.until.register import register
from tools.do_excel import DoExcel
from tools.logger import logger
from config.conf import DATA_DIR

do_excel = DoExcel(DATA_DIR, "register")
TestData = do_excel.get_data()
do_excel.close_file()


@pytest.mark.usefixtures("fix_class_level")
class TestOrder:

    @pytest.mark.usefixtures("fix_function_level")
    @pytest.mark.register
    @pytest.mark.parametrize("case", TestData)  # 读取excel文件中的测试用例
    def test_register(self, case):

        logger.info("测试数据：{}".format(eval(case["Data"])))
        logger.info("开始执行第 {} 条用例：{}！".format(case["CaseID"], case["Title"]))
        # print("开始执行第 {} 条用例：{}，测试数据：{}！".format(case["CaseID"], case["Title"], eval(case["Data"])))
        res = register(eval(case["Data"])["username"],
                       eval(case["Data"])["password1"],
                       eval(case["Data"])["password2"])
        logger.info("预期结果为：{}".format(eval(case["check"])))
        logger.info("实际运行结果为：{}".format(res))
        # 3、断言：预期结果与实际结果的比对
        try:
            # self.assertEqual(res, eval(case["check"]))
            assert res == eval(case["check"])
        except AssertionError:
            logger.exception("断言失败，第 {} 用例执行不通过！！".format(case["CaseID"]))
            raise
        else:
            logger.info("断言成功，第 {} 用例执行通过！".format(case["CaseID"]))

    @pytest.mark.usefixtures("fix_function_level")
    def test_a(self):
        logger.info("测试数字和字符串数字是否相等！")
        try:
            a = 1
            assert 1 is a
            assert 1 == '1'
        except AssertionError:
            logger.exception('测试数字和字符串数字是否相等失败！！')
            raise
        else:
            logger.info("测试数字和字符串是否相等通过！！")

    @pytest.mark.usefixtures("fix_function_level")
    def test_out_function(self):
        logger.info("测试数字和元组数字是否相等！！")
        try:
            assert 3 == (4,)
        except AssertionError:
            logger.exception("测试数字和元组数字是否相等失败！！")
            raise
        else:
            logger.info("测试数字和元组数字是否相等通过！！")


if __name__ == '__main__':
    pytest.main(['TestCase/test_03_order.py', '--alluredir=Outputs/allure'])
    os.system('allure serve Outputs/allure')

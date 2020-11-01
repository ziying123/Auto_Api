# web-UI 自动化测试示例

---

## 框架设计

- pytest
- selenium
- POM 模型

---

## 目录结构

    common                 ——公共类
    TestCase               ——测试用例
    conf.py                ——各种固定配置
    conftest.py            ——pytest胶水文件
    pytest.ini             ——pytest配置文件

---

## 运行

- `cd 项目目录`

* MacOS 系统或 Linux 系统

- 在命令行输入`sh run_mac.sh`即可运行

* Windows 系统

- 在命令行输入`run_mac.bat`即可运行


# allure参数说明


- allure --alluredir

- allure generate
    - -c 生成报告前删除上一次生成的报告
    - -o 指定生成的报告目录
- allure open
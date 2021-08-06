from HTMLTestRunner import HTMLTestRunner
import unittest
# 加载所有用例
tests = unittest.defaultTestLoader.discover(r"D:\Python 3.8.3\lx.2021.8.05", pattern="bank.py")

# 使用运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title="银行核心业务报告",
    description="工商银行核心业务的测试报告",
    verbosity=1,
    stream=open("bank.html", mode="w+", encoding="utf-8")
)

# 运行所有用例
runner.run(tests)
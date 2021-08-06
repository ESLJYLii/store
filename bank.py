from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from demo import Bank

# 新增用户数据源
addData = [
    [11111111, "li", 345123, "中国", "江苏", "山塘路", "x201", 800],
    [22222222, "田一", 1234789, "中国", "湖北", "武康路", "s99", 1000]
]
# 存钱数据源
save = [
    [2, 99],
    [1, 300]
]
# 取钱数据源
get = [
    [0, 798946, 900],
    [1, 1, 100]
]
# 转账数据源
trans = [
    [0, 1, 798946, 100],
    [1, 2, 1, 200]
]
# 查询数据源
query = [
    [1, 1],
    [2, 123456]
]
@ddt
class testBank(TestCase):
    @data(*addData)  # 引入数据源
    @unpack # 解包
    def testaddUser(self, account, username, password, country, province, street, gate, money):
        bank = Bank()
        bank.bank_addUser(account, username, password, country, province, street, gate, money)

    @data(*save)
    @unpack
    def testsaveMoney(self, account, saveMon):
        bank = Bank()
        bank.bank_saveMoney(account, saveMon)

    @data(*get)
    @unpack
    def testgetMoney(self, account, pwd, getMon):
        bank = Bank()
        bank.bank_getMoney(account, pwd, getMon)

    @data(*trans)
    @unpack
    def testtransferMoney(self, account, account1, pwd, transferMon):
        bank = Bank()
        bank.bank_transferMoney(account, account1, pwd, transferMon)

    @data(*query)
    @unpack
    def testquery(self, account, pwd):
        bank = Bank()
        bank.bank_query(account, pwd)
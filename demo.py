import pymysql
import random
import time

# 连接数据库
con = pymysql.connect(host="localhost", user="root", password="", database="bank")

# 创建控制台
cursor = con.cursor()


class Bank:

    # 银行的开户逻辑
    def bank_addUser(self, account, username, password, country, province, street, gate, money):
        bank_name = "中国工商银行昌平回龙观支行"  # 银行名称
        registerDate = time.strftime("%Y/%m/%d %H:%M:%S")
        sql = "select account from person"
        cursor.execute(sql)
        data = cursor.fetchall()
        length = len(data)
        # 1.判断数据库是否已满
        if length >= 100:
            return 3
        # # 2.判断用户是否存在
        cursor.execute("select account from person where account = %s" % account)
        data = cursor.fetchone()
        if data:
            return 2
        else:
            # 3.正常开户
            sql = "insert into person values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            param = [account, username, password, country, province, street, gate, money, registerDate, bank_name]
            cursor.execute(sql, param)
            con.commit()
            return 1

    # 银行的存钱逻辑
    def bank_saveMoney(self, account, saveMon):
        sql = "select * from person where account = %s"
        a = [account]
        cursor.execute(sql, a)
        data = cursor.fetchall()
        if data is None:
            return False
        else:
            sql = "update person set money = money + %s WHERE account = %s"
            param = [saveMon, account]
            cursor.execute(sql, param)
            con.commit()

    # 银行的取钱逻辑
    def bank_getMoney(self, account, pwd, getMon):
        cursor.execute("SELECT * FROM `person` where account = %s" % account)
        record = cursor.fetchone()
        if record is None:
            return 1
        if record[2] != pwd:
            return 2
        if getMon > record[7]:
            return 3

    # 银行的转账逻辑
    def bank_transferMoney(self, account, account1, pwd, transferMon):
        cursor.execute("SELECT * FROM `person` where account = %s" % account)
        record = cursor.fetchone()
        if record is None:
            return 1
        cursor.execute("SELECT * FROM `person` where account = %s" % account1)
        record = cursor.fetchone()
        if record is None:
            return 1
        if pwd != record[2]:
            return 2
        if transferMon > record[7]:
            return 3

    # 银行的查询逻辑
    def bank_query(self, account, pwd):
        cursor.execute("select * from person WHERE account = %s" % account)
        record = cursor.fetchone()
        if record is None:
            print('您输入的账号不存在！')
        else:
            if pwd != record[2]:
                print('您输入的密码不正确！')
            else:
                print('查询成功，您的个人信息如下:')
                info = '''
                            ----------个人信息----------
                            用户名：%s
                            密码：%s
                            账号：%s
                            地址信息
                                国家：%s
                                省份：%s
                                街道：%s
                                门牌号: %s
                            余额：%s
                            开户行地址：%s
                            ------------------------------
                        '''
                print(info % (record[1], record[2], record[0], record[3], record[4], record[5],
                              record[6], record[7], record[9]))

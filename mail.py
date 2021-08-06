import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

# def send_email():
sender = '1457934803@qq.com'  # 发件人邮箱账号
my_pass = 'ozdciyzidqmmidbi'  # 发件人邮箱授权码
user = '2956761599@qq.com'  # 收件人邮箱账号

msg = MIMEMultipart()  # 创建一个邮件
msg['From'] = formataddr(("李轩", sender))  # 括号里对应发件人邮箱昵称、发件人邮箱账号
msg['To'] = formataddr(("", user))  # 括号里对应收件人邮箱昵称、收件人邮箱账号
msg['Subject'] = "银行核心业务测试用例执行结果"  # 邮件的主题，也可以说是标题

server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，SMTP端口是25
server.login(sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码

# 发送附件
att = MIMEText(open('bank.html', 'rb').read(), 'base64', 'utf-8')  # 构造附件，三个参数：第一个为附件路径，第二个附件格式，第三个附件设置编码utf-8
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = "attachment; filename=file.html"  # filename为文件名字
msg.attach(att)

try:
    server.sendmail(sender, user, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()  # 关闭连接
    print("邮件发送成功")
except smtplib.SMTPException:
    print("邮件发送失败")
# -*- coding: utf-8 -*-
# __author__ = 'Carina'


# 附件格式
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import smtplib


if __name__ == "__main__":
    print("发送HTML邮件示例")

    # 邮件发送者
    sender = "zhangXXX@163.com"

    # 邮件接收地址列表
    receivers = "XXX@163.com"

    # 构建发送内容
    # 使用html标识发送内容为文本格式
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = receivers

    # 构建邮件标题
    msg["Subject"] = Header("Python", "utf-8")

    # 构建邮件正文内容
    msg.attach(MIMEText("Python学习", "plain", "utf-8"))

    # 构造附件，多个附件同理
    attach1 = MIMEText(open("D:\deeptest\第二期\杭州-张月萍\快学python3\learn openpyxl.py", 'rb').read(), "base64", "utf-8")
    attach1["Contype-Type"] = "application/octet-stream"

    # 这里filename随意写，将会在邮件中显示
    attach1["Contype-Disposition"] = "attachment:learn urllib=code.py"

    # 关联附件到邮件中
    msg.attach(attach1)

    # smtp服务
    smtpserver = "smtp.163.com"
    smtpport = 25

    # 发送人邮件用户名或专用于smtp账户用户名
    username = "zhangXXX"

    # 发送人邮件密码或专用于smtp账户的密码(客户端授权密码)
    password = "XXX"

    # 构建smtp对象
    smtp = smtplib.SMTP()

    # 连接到smtp服务
    con = smtp.connect(smtpserver, smtpport)
    print("连接结果：", con)

    # 登录smtp服务
    log = smtp.login(username, password)

    print("登录结果：", log)

    # 发送邮件
    print(receivers)
    res = smtp.sendmail(sender, receivers, msg.as_string())
    print("邮件发送结果：", res)

    # 退出
    smtp.quit()

    print("send email finish")

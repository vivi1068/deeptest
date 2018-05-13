# -*- coding: utf-8 -*-
# __author__ = 'Carina'


import smtplib
# 构建文本和html格式的邮件使用MIMEText构建
from email.mime.text import MIMEText
from email.header import Header


if __name__ == "__main__":
    print("发送文本邮件示例")

    # 邮件发送者
    sender = "zhangXXX@163.com"

    # 邮件接收地址列表
    receivers = "XXX@163.com"

    # 构建发送内容
    # MIMEText标识发送内容为文本格式
    # 使用plain标识文本内容格式
    #msg = MIMEText("python1", "plain", "utf-8")
    # 使用html标识发送内容为文本格式
    msg = MIMEText("<p>github</p><a href='https://github.com'>Github社区</a>", "html", "utf-8")
    msg["From"] = sender
    msg["To"] = receivers

    # 构建邮件标题
    msg["Subject"] = Header("Python", "utf-8")

    # smtp服务
    smtpserver = "smtp.163.com"
    smtpport =25

    # 发送人邮件用户名或专用于smtp账户用户名
    username = "zhangXXX"

    # 发送人邮件密码或专用于smtp账户的密码(客户端授权密码)
    password = "XXX"

    # 构建smtp对象
    smtp = smtplib.SMTP()

    # 连接到smtp服务
    con =smtp.connect(smtpserver, smtpport)
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
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/16 12:53
# @Author  : yulu
# @File    : smtp_study
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

if __name__ == "__main__":

    # 邮件发送者
    sender = "deep_test@126.com"

    # 邮件接收地址列表
    # 请讲XXX改为你的126邮箱名或整个改为你的目标接收邮箱地址
    receivers = "gonghuihui55@163.com"

    # 发送内容构建
    # text标识发送内容为文本格式
    # msg = MIMEText("微信公众号：开源优测", "Plain", "utf-8")
    msg = MIMEMultipart()
    msg1 = MIMEText("<p>微信公众号：开源优测</p><a href='http://www.testingunion.com'>开源优测社区</a>",
                    "html",
                    "utf-8")
    msg["From"] = "deep_test@126.com"
    msg["To"] = receivers

    # 构建邮件标题
    msg["Subject"] = Header("开源优测_DeepTest", "utf-8")

    # 构建邮件正文内容
    msg.attach(MIMEText("微信公众号：开源优测", "plain", "utf-8"))

    # 构建附件
    attach1 = MIMEText(open("set_study.py", 'rb').read(), "base64", "utf-8")
    attach1["Content-Type"] = "application/octets-stream"
    attach1["Content-Disposition"] = "attrachment;filename=code.py"
    msg.attach(attach1)

    # smtp服务
    smtpserver = "smtp.126.com"
    smtpport = 25

    # 发送人邮件用户名或专用smtp账户用户名
    username = "deep_test"

    # 发送人邮件密码或专用于smtp账户的密码
    password = "123456a"

    # 构建smtp对象
    smtp = smtplib.SMTP()

    # 连接到smtp服务
    con = smtp.connect(smtpserver,smtpport)
    print("连接结果", con)

    # 登录smtp服务
    log = smtp.login(username, password)
    print("登录结果", log)

    # 发送邮件
    print(receivers)
    res =smtp.sendmail(sender, receivers, msg.as_string())
    print("邮件发送结果", res)

    # 退出
    smtp.quit()
    print("send mail finish")


#!usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

# 发送简单邮件
mail_host = "smtp.163.com"
mail_user = "xxx@163.com"
mail_pass = "xxx"

sender = 'xxx@163.com' # 发件人邮箱
receivers = ['xxx@qq.com']    # 接收邮件的人们

content = 'Python 邮件发送测试'
title = '主题'
"""
message = MIMEText(content, 'plain', 'utf-8')
message['From'] = "{}".format(sender)
message['To'] = ",".join(receivers)
message['Subject'] = Header(title, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    con = smtpObj.connect(mail_host, 25)
    print(con)

    log = smtpObj.login(mail_user, mail_pass)
    print(log)
    
    smtpObj.sendmail(sender, receivers, message.as_string())
    print('seccess')
    smtpObj.quit
except smtplib.SMTPException as e:
    print(e)
    smtpObj.quit
"""
"""
# 发送HTML格式的邮件
# mail_msg = """
# <p>Python 邮件发送测试</p>
# <p><a href="http://www.baidu.com">链接</a></p>
"""
message1 = MIMEText(mail_msg, 'html', 'utf-8')
message1['From'] = "{}".format(sender)
message1['To'] = ",".join(receivers)
message1['Subject'] = Header(title, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    con = smtpObj.connect(mail_host, 25)
    print(con)

    log = smtpObj.login(mail_user, mail_pass)
    print(log)
    
    smtpObj.sendmail(sender, receivers, message1.as_string())
    print('seccess')
    smtpObj.quit
except smtplib.SMTPException as e:
    print(e)
    smtpObj.quit
"""

# 发送带附件的邮件
message2 = MIMEMultipart()
message2['From'] = "{}".format(sender)
message2['To'] = ",".join(receivers)
message2['Subject'] = Header(title, 'utf-8')

# 邮件正文内容
message2.attach(MIMEText(content, 'plain', 'utf-8'))

# 构造附件1
att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'

# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="text.txt"'
message2.attach(att1)

try:
    smtpObj = smtplib.SMTP()
    con = smtpObj.connect(mail_host, 25)
    print(con)

    log = smtpObj.login(mail_user, mail_pass)
    print(log)

    smtpObj.sendmail(sender, receivers, message2.as_string())
    print('success')
    smtpObj.quit
except smtplib.SMTPException as e:
    print(e)

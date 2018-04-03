# __author__ ='wuwa'
# -*- coding: utf-8 -*-

"""
email：构造邮件
1.发送邮件的账号、密码
2.连接邮件服务
3.设置邮件标题、内容
smtplib：发送邮件
4.发送邮件
"""
import os
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class WriteEmails:
    def __init__(self, smtp_server, stmp_port, sender, password, reveiver, subject, content, msg_type, attachment):
        self.smtp_server = smtp_server
        self.stmp_port = stmp_port
        self.sender = sender
        self.password = password
        self.reveiver = reveiver
        self.subject = subject
        self.content = content
        self.msg_type = msg_type
        self.attachment = attachment

    def __content_of_email(self, msg_type):
        """
        邮件正文为文本内容
        :param content:
        :return:
        """
        msg = MIMEMultipart()
        msg["From"] = self.sender
        msg["To"] = ";".join(self.reveiver)
        msg['Subject'] = Header(self.subject, "utf-8")

        # 如果msg为plain,则邮件正文为文本
        if msg_type == 'plain':
            msg.attach(MIMEText(self.content, "plain", "utf-8"))
        # 如果msg为html,则邮件正文为html
        elif msg_type == "html":
            msg.attach(MIMEText(self.content, "html", "utf-8"))
        else:
            print("邮件内容类型不正确")

        if self.attachment is not None:

            # 读取附件内容
            with open(attachment, 'r')as f:
                contents = f.read()
            # 设置html格式参数
            html_content = MIMEText(contents, 'base64', 'utf-8')
            html_content["Content-Type"] = 'application/octet-stream'
            html_content.add_header("Content-Disposition", "attachment", filename=os.path.basename(attachment))
            msg.attach(html_content)

        return msg

    def senf_send_email(self):
        """
        发邮件
        :return: 
        """
        msg = self.__content_of_email(self.msg_type)

        try:
            # 构建smtp对象
            smtp = smtplib.SMTP()

            # 连接到smtp服务
            smtp.connect(self.smtp_server, self.stmp_port)

            # 登录smtp服务
            smtp.login(self.sender, self.password)

            # 发送邮件
            print('收件人为：', self.reveiver)
            res = smtp.sendmail(self.sender, self.reveiver, msg.as_string())
            print("邮件发送结果： ", res)

            # 退出
            smtp.quit()
            print("send email finish")

        except smtplib.SMTPException as e:
            print('error', e)


if __name__ == "__main__":

    # 邮箱服务地址
    smtp_server = 'xx.xx.com'
    # 邮箱服务的端口
    stmp_port = xx

    # 邮件发送者
    sender = "xxxx@qq.com"
    # 邮件发送者密码
    password = "password"

    # 邮件接收者
    receiver = ["xxx@qq@qq.com", "xxx@qq.com"]
    content = "邮件正文"
    subject = "邮件标题"

    # 邮件正文类型
    msg_type = "html"
    BASE_DIR = os.path.abspath(os.path.dirname(os.getcwd()))
    # 获取ini文件的路径
    attachment = os.path.join(BASE_DIR, "report\\report.html")

    # 实例化
    m = WriteEmails(smtp_server, stmp_port, sender, password, receiver, subject, content, msg_type, attachment)
    # 调用类方法
    m.senf_send_email()

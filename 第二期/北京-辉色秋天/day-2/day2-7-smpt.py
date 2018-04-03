#-*-coding:utf-8-*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

def send_email(msg):

    sender="xxxx"
    reiceiver = "xxx"

    msg['From'] = "小鹿乖乖"
    msg["To"] = reiceiver

    smtpserver = "smtp.qiye.163.com"
    smtpport= 25
    username = "xxxx"
    password = "xxxxxx"
    smtp = smtplib.SMTP()
    cnn = smtp.connect(smtpserver,smtpport)
    print("连接结果： ", cnn)

    log = smtp.login(username, password)
    print("登录结果：", log)

    res = smtp.sendmail(sender, reiceiver,msg.as_string())
    print("邮件发送结果： ", res)
    smtp.quit()
    

def test_t():
    print("发送文本邮件")
    #msg=MIMEText("这是测试邮件",'plain', 'utf-8')
    msg = MIMEText("<p>微信公众号号：开源优测</p><a href='http://www.testingunion.com'>开源优测社区</a>>","html", "utf-8")

    msg['Subject']=Header("zheshi ceshi youjian", 'utf-8')

    send_email(msg)


def attach_t():
    print("发送附件")
    msg = MIMEMultipart()
    
    msg['Subject']=Header("zheshi ceshi youjian", 'utf-8')

    msg.attach(MIMEText("这是测试邮件",'plain', 'utf-8'))
    attchq = MIMEText(open("data_demo-1.xml",'rb').read(),"base64",'utf-8')

    attchq["Content-Type"] = "application/octet-stream"

    attchq['Content-Disposition']= "attachment;filename=data_demo-1.xml"

    msg.attach(attchq)
    send_email(msg)
if __name__ == "__main__":
    test_t()
    attach_t()

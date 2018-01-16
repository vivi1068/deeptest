__author__='棒棒糖'
import smtplib
from email.mime.text  import MIMEText
from email.header import Header
from email.mime.multipart import  MIMEMultipart

if __name__=='__main__':
    print('发送文本邮件示例')
    #邮件发送者
    sender='deep_test@126.com'
    #y邮件接收者
    receivers='879106261@qq.com'
    #构造MIMEMultipart对象做为根容器,再将文本，附件添加到根容器
    msg = MIMEMultipart()
    msg['From']=sender
    msg['To']=receivers
    #构建邮件标题
    msg['Subject']=Header('就服你','utf-8')
    # 发送内容构建
    # text标识发送内容为文本格式
    #msg=MIMEText('棒棒糖碰一个','plain','utf-8')
    msg.attach(MIMEText("<p>棒棒糖</p><a href='http://www.testingunion.com'>棒棒糖社区</a>>",
                   "html",
                   "utf-8"))
    #加附件
    attach1=MIMEText(open('SMTP_test.py','rb').read(),'base64','utf-8')
    attach1['Content-Type']='application/octet-stream'
    #这里filename随意写，将会在邮件中显示
    attach1['Content-Disposition']='attrachment:filename=code.py'
    #关联附件到邮件中
    msg.attach(attach1)

    #smtp服务
    smtpserver='smtp.126.com'
    smtpport=25
    #发送人邮件用户名或专用于smtp账户用户名
    username='deep_test'
    # 发送人邮件密码或专用于smtp账户的密码
    password='123456a'
    #构建smtp对象
    smtp=smtplib.SMTP()
    # 构建smtp对象
    con=smtp.connect(smtpserver,smtpport)
    print('链接结果：',con)
    #登录smtp服务
    log=smtp.login(username,password)
    print('登录结果：',log)
    #发送邮件
    print(receivers)
    res=smtp.sendmail(sender,receivers,msg.as_string())
    print('邮件发送结果：',res)
    #退出
    smtp.quit()
    print('send email finish')

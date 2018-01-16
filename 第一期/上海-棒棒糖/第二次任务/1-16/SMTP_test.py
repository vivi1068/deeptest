# 创建smtp对象smtp = smtplib.SMTP([host [, port [, localhost]]] )

# 参数说明
# host： smtp服务地址，例如126邮箱的是：smtp.126.com
# port： smtp服务端口
# localhost： 如果你的smtp服务在本机，则只需指定localhost即可


# 发送邮件函数SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options])

# 参数说明
# from_addr： 邮件发送地址
# to_addrs： 邮件接收地址列表
# msg： 邮件内容
# mail_options, rcpt_options  可选参数，暂时不需要了解

__author__='棒棒糖'
import smtplib
from email.mime.text  import MIMEText
from email.header import Header

if __name__=='__main__':
    print('发送文本邮件示例')
    #邮件发送者
    sender='deep_test@126.com'
    #y邮件接收者
    receivers='879106261@qq.com'
    # 发送内容构建
    # text标识发送内容为文本格式
    #msg=MIMEText('棒棒糖碰一个','plain','utf-8')
    msg = MIMEText("<p>棒棒糖</p><a href='http://www.testingunion.com'>棒棒糖社区</a>>",
                   "html",
                   "utf-8")
    msg['From']=sender
    msg['To']=receivers
    #构建邮件标题
    msg['Subject']=Header('就服你','utf-8')
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

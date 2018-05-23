import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = 'yyz@sensedeal.ai'  # 发件人邮箱账号
my_pass = 'xPetVmmkCgfmdDfN'  # 发件人邮箱密码
my_user = 'yyz@sensedeal.ai'  # 收件人邮箱账号，我这边发送给自己


# def mail():
#     ret = True
#     try:
#         msg = MIMEText('pdf2Mysql is done', 'plain', 'utf-8')
#         msg['From'] = formataddr(["cwAutoEmail", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
#         msg['To'] = formataddr(["myself", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
#         msg['Subject'] = "pdf2Mysql is done"  # 邮件的主题，也可以说是标题
#
#         server = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
#         server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
#         server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
#         server.quit()  # 关闭连接
#     except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
#         ret = False
#     return ret

def mail(content):
    ret = True
    try:
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr(["yyzAutoEmail", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["myself", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "newsMysql is done"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret

# ret = mail('若运行完成')
# if ret:
#     print("邮件发送成功")
# else:
#     print("邮件发送失败")
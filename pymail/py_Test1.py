# -*- coding:utf-8 -*-
from __future__ import print_function

__author__ = 'yhwang'
__version__ = '1.0'

import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = "smtp.aliyun.com"
mail_user = "linhumao@foxmail.com"
mail_pass = "2768398535@qq.com"

sender = '2768398535@qq.com'
receivers = ['2768398535@qq.com']

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("123", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

for receiver in receivers:
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, port=465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receiver, message.as_string())
        smtpObj.quit()
        print(u"%s邮件发送成功" % receiver)
    except smtplib.SMTPException:
        print(u"Error: 发送%s邮件失败" % receiver)

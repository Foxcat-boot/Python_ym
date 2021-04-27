def send():
    # coding:utf-8

    """
    使用SMTP服务发送邮件
    """

    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header

    receivers = input("请输入发送邮箱:")
    remembermail = receivers
    theme = input("请输入主题:")
    content = input("请输入发送内容(暂不支持换行):")
    """
    发送内容如果需要换行,请在代码中修改
    输入"\n"换行
    """
    # content = "如果你收到这条消息,说明测试成功 \nIf you receive this message, the test is successful"

    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "2768398535@qq.com"  # 用户名
    mail_pass = "ksphmdbcexlzdfge"  # 口令,QQ邮箱是输入授权码，在qq邮箱设置 里用验证过的手机发送短信获得，不含空格

    sender = '2768398535@qq.com'
    # receivers = ['1990746148@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    """
    需要批量发送,请在代码中修改
    """
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header("???", 'utf-8')
    message['To'] = Header("you", 'utf-8')

    subject = theme

    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print(u"邮件发送成功")

    except smtplib.SMTPException as e:
        print(u"邮件发送失败")


send()

while True:
    inp = input("是否再次发送?(y/n)")
    if inp == "y":
        send()
        continue
    elif inp == "n":
        exit()
    else:
        print("输入错误,请重新输入")
        continue

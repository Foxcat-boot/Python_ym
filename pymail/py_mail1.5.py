import http.client
import time
import os
import socket

z = "2021-1-31"  # 到期时间
zh = "2"  # 账号
mm = "1"  # 密码


def isNetOK(testserver):
    s = socket.socket()
    s.settimeout(3)
    try:
        status = s.connect_ex(testserver)
        if status == 0:
            s.close()
            return True
        else:
            return False
    except Exception as e:
        return False



def isNetqqmailOK(testserver=('mail.qq.com', 443)):
    isOK = isNetOK(testserver)
    return isOK


def isNetbaiduOK(testserver=('www.baidu.com', 443)):
    isOK = isNetOK(testserver)
    return isOK


def main():
    qqmail = isNetqqmailOK()
    # print(qqmail)
    baidu = isNetbaiduOK()
    # print(baidu)


main()


def gettime(host):
    conn = http.client.HTTPConnection(host)
    conn.request("GET", "/")
    r = conn.getresponse()
    # r.getheaders()  #获取所有的http头/Gets all HTTP headers
    ts = r.getheader('date')  # 获取http头date部分/Gets the HTTP header Date part
    # 将GMT时间转换成北京时间/Convert GMT time to Beijing time
    ltime = time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
    # print(ltime)
    ttime = time.localtime(time.mktime(ltime)+8*60*60)
    # print(ttime)
    dat = "date %u-%02u-%02u" % (ttime.tm_year,ttime.tm_mon,ttime.tm_mday)
    tm = "time %02u:%02u:%02u" % (ttime.tm_hour,ttime.tm_min,ttime.tm_sec)
    # print(dat, tm)
    os.system(dat)
    os.system(tm)
gettime('www.baidu.com')


a = z  # 到期时间
a2 = time.strptime(a, '%Y-%m-%d')
localtime = time.localtime(time.time())  # 本地时间
if a2 >= localtime:
    timepass = 1
else:
    timepass = 0


def cn():
    def send():
        # coding:utf-8

        """
        使用SMTP服务发送邮件
        """

        import smtplib
        from email.mime.text import MIMEText
        from email.header import Header

        receivers = input("请输入发送邮箱:")
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
        elif inp == "Y":
            send()
            continue
        if inp == "n":
            exit()
        elif inp == "N":
            exit()
        else:
            print("输入错误,请重新输入")
            continue


def en():
    def send():
        # coding:utf-8

        """
        Use SMTP service to send mail
        """

        import smtplib
        from email.mime.text import MIMEText
        from email.header import Header

        receivers = input("Please enter the email address:")
        theme = input("Please enter the subject:")
        content = input("Please enter send content (line wrapping is not supported):")
        """
        Send content If you need a line break, change it in your code
        Type "\n" to wrap
        """
        # content = "如果你收到这条消息,说明测试成功 \nIf you receive this message, the test is successful"

        # Third-party SMTP services
        mail_host = "smtp.qq.com"  # Setup server
        mail_user = "2768398535@qq.com"  # The user name
        mail_pass = "ksphmdbcexlzdfge"  # Password,QQ mailbox is to enter the authorization code,
        # in the QQ mailbox Settings with a verified mobile phone to send SMS, no space

        sender = '2768398535@qq.com'
        # receivers = ['1990746148@qq.com']  # To receive mail, you can set it to your QQ mailbox or other mailboxes
        """
        Need to batch send, please modify in the code
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
            print(u"Email sent successfully")

        except smtplib.SMTPException as e:
            print(u"Email failed to send")

    send()

    while True:
        inp = input("Whether to send again?(y/n)")
        if inp == "y":
            send()
            continue
        elif inp == "Y":
            send()
            continue
        elif inp == "n":
            exit()
        elif inp == "N":
            exit()
        else:
            print("Input error, please retype")
            continue


def cnStar():
    while True:
        cnchoose = input('此程序需要连接网络并校准系统时间,同意请按"a",不同意并退出请按"d"')
        if cnchoose == "a":
            cnUsWD()
        elif cnchoose == "A":
            cnUsWD()
        elif cnchoose == "d":
            exit()
        elif cnchoose == "D":
            exit()
        else:
            print("输入错误,请重新输入")
            continue


def cnUsWD():
    while True:
        cnUser = input("请输入用户名:")
        if cnUser == zh:
            print("通过用户名检测,正在进入密码检测...")
            cnPsWD()
        else:
            print("用户名输入错误,请重新输入")
            continue


def cnPsWD():
    while True:
        cnPassword = input("请输入密码:")
        if cnPassword == mm:
            while True:
                if timepass == 1:
                    os.system('cls')
                    print("通过密码检测,允许进入系统...")
                    cn()
                else:
                    print("此版本已过期,请重新下载最新版本")
                    break
        else:
            print("密码输入错误,请重新输入")
            continue


def enStar():
    while True:
        cnchoose = input('This program needs to connect to the network '
                         'and calibrate the system time. If you agree, please press "a". '
                         'If you disagree and exit, please press "d".')
        if cnchoose == "a":
            enUsWD()
        elif cnchoose == "A":
            enUsWD()
        elif cnchoose == "d":
            exit()
        elif cnchoose == "D":
            exit()
        else:
            print("Input error, please retype")
            continue


def enUsWD():
    while True:
        enUser = input("Please enter user name:")
        if enUser == zh:
            print("Through user name detection, entering password detection...")
            enPsWD()
        else:
            print("User name input error, please retype")
            continue


def enPsWD():
    while True:
        enPassword = input("Please enter your password:")
        if enPassword == mm:
            print("Password detection allows access to the system...")
            while True:
                if timepass == 1:
                    os.system('cls')
                    en()
                else:
                    print("This version has expired. Please download the latest version again")
                    break
        else:
            print("The password is incorrect. Please re-enter it")
            continue


def START():
    while True:
        language = input("界面语言/UI language:(cn/en):")
        if language == "en":
            enStar()
        elif language == "cn":
            cnStar()
        else:
            print("输入错误,请重新输入/Input error, please retype")
            continue


if isNetqqmailOK() and isNetbaiduOK():
    START()

input("请按任意键退出.../Please press any key to exit...")
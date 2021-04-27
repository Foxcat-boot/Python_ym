import socket


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
    print(qqmail)
    baidu = isNetbaiduOK()
    print(baidu)


# if __name__ == '__main__':
main()

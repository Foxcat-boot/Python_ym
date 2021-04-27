num1 = int(input("请输入打印次数:"))

char1 = input("请输入需要打印的字符:")

row = int(input("请输入打印行数:"))

def print_(char, num):
    """定义函数每一行打印的字符串

    :param char: 打印的字符
    :param num: 打印的次数
    """
    print(char * num)

def print_ls(row1):

    a = 1

    while a <= row:

        print_(char1 , num1),

        a += 1

print_ls(row)
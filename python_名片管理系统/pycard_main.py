import os
import pycard_tools
while True:

    pycard_tools.show_menu()

    a = "1"

    choose1 = input("请选择希望执行的操作:")

    try:
        choose = int(choose1 + a)

        ch = int((choose - 1) / 10)
    except:
        continue

    print("选择的操作是[%s]" % ch)

    if choose == 91:
        os.system('cls')
        print("欢迎再次使用[名片管理系统]")
        break

    elif choose == 11:
        os.system('cls')
        pycard_tools.new_card()

    elif choose == 21:
        os.system('cls')
        pycard_tools.show_all()

    elif choose == 31:
        os.system('cls')
        pycard_tools.search_card()

    else:
        os.system('cls')
        print("输入错误,请重新输入...")

input("按回车键退出...")
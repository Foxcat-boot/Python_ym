import os
print("用户名:Temp")
# os.system('cls' if os.name == 'nt' else 'clear')


def a():
    USA = ""
    while True:
        USB = input("密码:")
        if USB == USA:
            print("进入System...")
            break
        else:
            print("密码错误")
            # os.system('cls' if os.name == 'nt' else 'clear')
            os.system("clear")
            continue


a()

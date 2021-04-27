# -*- coding:utf-8 -*-
# coding=utf-8

import random
import msvcrt
import os

print("Windows关机程序")
print("在关机前有5次确认,输入给出数字以确认,否则将退出程序")


def first(number):
    random1 = random.randint(1, 9)
    print(random1)
    UserInput = int(input("是否要关机(确认次数%d):" % number))
    if random1 == UserInput:
        pass
    else:
        print("已取消关机,按任意键退出")
        ord(msvcrt.getch())
        exit()


a = 1
while a < 5:
    first(a)
    a += 1

name = random.randint(1, 9)
print(name)
b = int(input("是否要关机(最后一次确认):"))
if name == b:
    # print("TurnDown")
    os.system('shutdown -p')
else:
    print("已取消关机,按任意键退出")
    ord(msvcrt.getch())

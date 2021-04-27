# -*- coding: utf-8 -*-
"""
Error
"""
import os
from PIL import ImageGrab
import datetime

now = datetime.datetime.now()
time = now.strftime("%Y-%m-%d %H-%M-%S")

nowdir = os.getcwd()  # 获取当前目录
disk = str(nowdir[0])  # 提取当前目录第一个字母,即盘符

pc = ImageGrab.grab()  # 获取当前屏幕快照,即截屏
# pc.save('D:\\12.png')  # 将屏幕截图保存到D盘下

dir_name = '%s:\\截图\\' % disk  # 将目录设为当前盘符根目录下"截图"文件夹中
dir_name_str = str(dir_name)
if not os.path.exists('%s:' % disk):  # 如果当前目录下没有"截图"这个文件夹
    os.mkdir("截图")  # 新建"截图"文件夹
needdir = dir_name_str + time
lastdir = str(needdir)
# TODO
pc.save(lastdir + ".png")
# z = str(time)
# x = str(lastdir + ".png")
# pc.save(x)
# 将截图保存至当前目录的"截图"文件夹中

# -*- coding: utf-8 -*-
from PIL import ImageGrab
import datetime
import os

now = datetime.datetime.now()
time = now.strftime("%Y-%m-%d %H-%M-%S")

pc = ImageGrab.grab()
# pc.save('12.png')

nowdir = os.getcwd()
disk = str(nowdir[0])

if not os.path.exists(r"%s:\\photo" % disk):
    os.mkdir(r"%s:\\photo" % disk)

dir_name = str('%s:\\photo\\%s.png' % (disk, time))

pc.save(dir_name)

input("按Enter退出")

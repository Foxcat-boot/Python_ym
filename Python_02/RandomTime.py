import time
import os
import datetime
from time import time, localtime, strftime
import random

input("")


def radom():
    a = localtime(time())
    s = int(strftime("%S", a))  # second
    y = int(strftime("%y", a))  # year
    m = int(strftime("%M", a))  # minute

    ints = (((((m * 224) + 392) * y + m) / s) * 0.73229) * 7
    float1 = float(float(ints) % 1)

    a = str("{:.3f}".format(float1))
    # a = 0.1 * float(a)
    print(a)



def kaishi():
    star = datetime.datetime.now()
    os.system('pause')
    touch = datetime.datetime.now()


radom()



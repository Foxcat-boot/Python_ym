import os

import sys

f_handler = open('out.log', 'w')

oldstdout = sys.stdout

sys.stdout = f_handler

print("start")

os.system('cls')

sys.stdout = oldstdout

print("123")

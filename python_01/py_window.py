# -*- coding: utf-8 -*-

import tkinter as tk

WD = tk.Tk()

width = WD.winfo_screenwidth()
heigh = WD.winfo_screenheight()

c = 500
k = 300

x = (width-c) / 2
y = (heigh-k) / 2
WD.geometry("%dx%d+%d+%d" % (c, k, x, y))

# WD.resizable(False, False)
WD.resizable(width=False, height=False)

WD.title("Welcome")

# WD.geometry("500x300")

L = tk.Label(WD, text='Hello! this is Me',
             bg='white', font=('Arial', 15), width=30, height=3)

e1 = tk.Entry(WD, show=None, font=('Arial', 14))   # 显示成密文形式
e2 = tk.Entry(WD, show=None, font=('Arial', 14))  # 显示成明文形式
e3 = tk.Entry(WD, show=None, font=('Arial', 14))

e2.pack()
e1.pack()
e3.pack()
chick = False
L.pack()

# TODO


def chick_me():

    if e2 == "1" and e1 == "2":
        e3.insert("insert", "Passed1")


    else:
        e3.insert("insert", "Error0")



b = tk.Button(WD, text='chick me', font=('Arial', 12), width=10, height=1, command=chick_me())
b.pack()


WD.mainloop()

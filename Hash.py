# -*- coding:utf-8 -*-
# coding=utf-8
import hashlib  # 导入hashlib模块
import tkinter
import tkinter.messagebox
import tkinter.filedialog
from tkinter import *


def hash(file_path, Bytes=1024):
    md5_1 = hashlib.md5()  # 创建一个md5算法对象证明其确实
    with open(file_path, 'rb') as f:  # 打开一个文件，必须是'rb'模式打开
        while 1:
            data = f.read(Bytes)  # 由于是一个文件，每次只读取固定字节
            if data:  # 当读取内容不为空时对读取内容进行update
                md5_1.update(data)
            else:  # 当整个文件读完之后停止update
                break
    ret = md5_1.hexdigest()  # 获取这个文件的MD5值
    return ret


# print(hash(r'E:/lujianfeiGitWork/sae/1/json/mnb/apk/plugin1.apk'))

def clickbrowser():
    filenames = tkinter.filedialog.askopenfilenames()
    if len(filenames) != 0:
        path.set(filenames[0])
    pass


def clickfun(file_path):
    if file_path == "":
        tkinter.messagebox.showinfo(title='提示', message='请输入文件路径')
        return
    output.set(hash(file_path))
    pass


top = tkinter.Tk()
top.resizable(0, 0)  # 防止用户调整尺寸
top.title("文件 hash 值计算")
path = StringVar(top, value='')
output = StringVar(top, value='')

label = tkinter.Label(top, text='输入文件路径：')
inputEntry = tkinter.Entry(top, width=50, textvariable=path)
btBrowser = tkinter.Button(top, text="浏览", command=lambda: clickbrowser())
btClick = tkinter.Button(top, text="计算文件 hash", command=lambda: clickfun(inputEntry.get()))
olabel = tkinter.Label(top, text='输出 hash：')
outputEntry = tkinter.Entry(top, width=50, textvariable=output)

label.grid(row=0, column=0)
inputEntry.grid(row=0, column=1)
btBrowser.grid(row=0, column=2)
olabel.grid(row=1, column=0)
outputEntry.grid(row=1, column=1)
btClick.grid(row=1, column=2)

col_count, row_count = top.grid_size()

# 进入消息循环
top.mainloop()
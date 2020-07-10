# 导入需要用到的模块
import webbrowser
import time
#import requests
import codecs
import os
# coding = utf-8
import tkinter
import tkinter as tk

win = tk.Tk()
win.title('科学大世界脚本控件v1.0')
win.geometry('600x600')
 
l = tkinter.Label(win, 
    text='滑动浏览执行记录!',    # 标签的文字
    bg='green',                 # 背景颜色
    font=('Arial', 12),         # 字体和字体大小
    width=15, height=2          # 标签长宽
    )
l.pack()
text = tkinter.Text(win,width=100,height=30)
text.pack()
def hit_me():
    i=1
    with open("jb1.txt",'r',encoding='UTF-8') as fp:
        for ebayno in fp:
            if i==1:
                h=ebayno.strip()
                i=i-1
                continue
            url = h+ebayno.strip()
            time.sleep(1) #打开间隔时间
            webbrowser.open(url)
            print("Open Success",url)
            str1 = url+'\n'

            text.insert(tkinter.INSERT,str1)



b = tk.Button(win, text='执行', font=('Arial', 12), width=10, height=1, command=hit_me)
b.pack()
win.mainloop()


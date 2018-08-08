# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import tkinter as tk


'''
显示一个可响应事件的菜单类 Menu.
'''

window = tk.Tk()
window.geometry('200x200')

lbl = tk.Label(window, text='', bg='yellow')
lbl.pack()

count = 0
def do_job():
	global count
	lbl.config(text='do ' + str(count))
	count += 1

# 创建一个 Menu 对象.
menubar = tk.Menu(window)

# 创建一个子 Menu. 设置 teaoff=0, 外观更美观. 
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
# 显示时有一条分割线.
filemenu.add_separator()
# window.quit 是内置于类 window 中的方法, 被
# 触发时自动关闭窗口.
filemenu.add_command(label='Exit', command=window.quit)

# 创建 "子子" menu.
submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='Import', menu=submenu, underline=0)
submenu.add_command(label='Submenu', command=do_job)

window.config(menu=menubar)
window.mainloop()










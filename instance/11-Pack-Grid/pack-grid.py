# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import tkinter as tk

'''
'''

window = tk.Tk()
window.geometry('200x200')

# pack 的参数 side 可以指定上下左右:
#	top, bottom, left, right
# tk.Label(window, text=1).pack(side='top')
# tk.Label(window, text=1).pack(side='bottom')
# tk.Label(window, text=1).pack(side='left')
# tk.Label(window, text=1).pack(side='right')

# Grid 是表格放置. 还可以通过 padx, pady 添加间隔.
# for i in range(0, 4):
# 	for j in range(0, 3):
# 		tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10)

# 指定坐标放置. anchor 指示锚置.
tk.Label(window, text=1).place(x=10, y=100, anchor='nw')

window.mainloop()
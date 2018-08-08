# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import tkinter as tk


'''
Frame 是一种底层的部件, 相当于窗口的窗口.
不直接可见, 用于管理部件.
'''

window = tk.Tk()
window.title('My Window')
window.geometry('200x200')

tk.Label(window, text='on the window').pack()

# 创建一个 Frame 框架类.
frm = tk.Frame(window)
frm.pack()

frm_l = tk.Frame(frm, )
frm_r = tk.Frame(frm, )

tk.Label(frm_l, text='on the frm_l1').pack()
tk.Label(frm_l, text='on the frm_l2').pack()
tk.Label(frm_r, text='on the frm_r').pack()

frm_l.pack(side='left')
frm_r.pack(side='right')

window.mainloop()
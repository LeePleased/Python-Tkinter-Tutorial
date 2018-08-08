# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import tkinter as tk


'''
显示一个拖动栏, 并将位置实时打印到 label 上.
'''

window = tk.Tk()
window.title('My Window')
window.geometry('200x200')

def print_selection(v):
	lbl.config(text='you have reached ' + v)

lbl = tk.Label(
		window,
		bg='yellow',
		width=20,
		text='empty'
	)

# 创建一个 Scale 拖动滚条对象. 其中参数 from_(为
# 避免与关键字 from 重名), to 表示滚动条的最小最大
# 值; 而 orient 指示滚条的方向; length 指示长度,
# 且以像素为单位; resolution 分辨率我理解是用来表示
# 小数位的; 而 showvalue=1 在条目上方时显示值.
s = tk.Scale(
		window,
		label='            drag me along',
		from_ = 5,
		to = 11,
		orient=tk.HORIZONTAL,
		length=200,
		showvalue=0,
		tickinterval=2,
		resolution=0.01,
		command=print_selection
	)

lbl.pack()
s.pack()

window.mainloop()

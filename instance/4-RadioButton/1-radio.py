# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import tkinter as tk


'''
显示一个复项单选框. 有多个选项, 但是每次只能选择一个
栏目, 然后打印到标签上.
'''

window = tk.Tk()
window.title('My Window')
window.geometry('200x200')

var = tk.StringVar()
lbl = tk.Label(
		window,
		bg='yellow',
		width=20,
		text='empty'
	)

def print_selection():
	# 除了 textvatiable, 另一种动态显示 label 的方法
	# 就是调用方法 config.
	lbl.config(text='You have selected ' + var.get())

# 这些 RadioButton 是以 var 为标准单选的.
rA = tk.Radiobutton(
		window,
		text='Option A',
		variable=var, value='A',
		command=print_selection
	)
rB = tk.Radiobutton(
		window,
		text='Option B',
		variable=var, value='B',
		command=print_selection
	)
rC = tk.Radiobutton(
		window,
		text='Option C',
		variable=var, value='C',
		command=print_selection
	)

lbl.pack()
rA.pack()
rB.pack()
rC.pack()

window.mainloop()

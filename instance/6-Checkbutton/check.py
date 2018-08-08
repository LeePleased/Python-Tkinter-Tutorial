# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import tkinter as tk


'''
'''

window = tk.Tk()
window.geometry('200x200')

lbl = tk.Label(window, bg='blue', width=20, text='empty')

def print_selection():
	if var1.get() is True and var2.get() is True:
		lbl.config(text='I love both')
	elif var1.get() is not True and var2.get() is True:
		lbl.config(text='I only love C++')
	elif var1.get() is True and var2.get() is not True:
		lbl.config(text='I only love Python')
	else:
		lbl.config(text='I do not love either')


var1 = tk.BooleanVar()
var2 = tk.BooleanVar()

# 创建复选按钮 CheckButton, 它的参数很大程度上
# 可以参考单选按钮 RadioButton.
c1 = tk.Checkbutton(
		window,
		text='Python',
		variable=var1,
		onvalue=True,
		offvalue=False,
		command=print_selection
	)
c2 = tk.Checkbutton(
		window,
		text='C++',
		variable=var2,
		onvalue=True,
		offvalue=False,
		command=print_selection
	)

lbl.pack()
c1.pack()
c2.pack()

window.mainloop()
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import tkinter as tk


'''
使用一个 Button 类引入事件函数 command 动态
展示 label 的内容. 
'''

window = tk.Tk()
window.title('My Window')
window.geometry('200x200')

# Tkinter 中包含许多这样的包装类, 类似还有
# IntVar, FloatVar 等.
varStr = tk.StringVar()
lbl = tk.Label(
		window,
		textvariable=varStr, # 由于标签是动态的, 应该用 variable.
		bg='green',
		font=('Arial', 12),
		width=15, height=2
	)
lbl.pack()

# 定义相应事件的函数.
on_hit = True
def hit_me():
	global on_hit
	if on_hit == True:
		on_hit = False
		varStr.set('')
	else:
		on_hit = True
		varStr.set('Hello Tkinter')

# 定义按钮 button.
b = tk.Button(
		window,
		text='Click me',
		width=15, height=2,
		command=hit_me
	)
b.pack()

window.mainloop()













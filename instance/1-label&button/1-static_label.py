# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import tkinter as tk


'''
显示一个静态不动的 Label 对象.
'''

# 每个 Tkinter-GUI 都应该包含一个窗口.
window = tk.Tk()
# 窗口的内容, 尺寸.
window.title('My Window')
window.geometry('200x100')

# Tkinter 中的类均是大写开头的, 这里是 
#Label, 标签类.
l = tk.Label(
		text='Hello Tkinter', # 标签文字.
		bg='yellow', # Background 背景.
		font=('Arial', 12), # 字体.
		width=15, height=2
	)
# 固定窗口位置.
l.pack() 

# 这个是必要的, 它相当于每间隔 1 毫秒
# 更新一次画布.
window.mainloop()
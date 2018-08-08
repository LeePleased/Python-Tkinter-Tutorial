# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import tkinter as tk

'''
创建一个输入框, 文本框. 按下按钮后将输入框的
值输入到文本框中.
'''

window = tk.Tk()
window.title('My Window')
window.title('200x200')

# 定义相应函数.
def insert_point():
	# 从输入框 entry 中获取文本.
	var = e.get()
	# 向输入文本 Text 中输入文本,
	# 其中 insert 表示即时插入.
	t.insert('insert', var)

def insert_end():
	var = e.get()
	# end 表示尾部插入.
	t.insert('end', var)


bp = tk.Button(
		window,
		text='insert point',
		command=insert_point
	)
be = tk.Button(
		window,
		text='insert end',
		command=insert_end
	)

# 创建一个输入框, show 表示显示. 类似
# 你输密码, 当 none 时现实原输入.
e = tk.Entry(window, show='*')

# 创建一个文本框用于显示.
t = tk.Text(window, height=, width=20)

e.pack()
bp.pack()
be.pack()
t.pack()

window.mainloop()

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import tkinter as tk

'''
创建一个复选框, 按下按钮后, 将所选字符串打印
到标签上.
'''

window = tk.Tk()
window.title('My Window')
window.geometry('200x200')

var = tk.StringVar()
lbl = tk.Label(
		window,
		bg='yellow',
		width=8, height=1,
		textvariable=var
	)

# 定义相应事件.
def print_selection():
	# lb: listbox, 从 listbox 中当前选中
	# 的 item 输出.
	val = lb.get(lb.curselection())
	var.set(val)

b = tk.Button(
		window,
		text='print selection',
		width=15, height=1,
		command=print_selection
	)

list_var = tk.StringVar()
# 为变量设置值.
list_var.set((11, 22, 33, 44))

# 创建 Listbox.
lb = tk.Listbox(window, listvariable=list_var)

# 从最后的位置插入元素.
list_items = [1, 2, 3, 4]
for item in list_items:
	lb.insert('end', item)

# 从第 1 个位置插入(从头是 0).
lb.insert(1, 'first')
# 从第 2 个位置插入.
lb.insert(2, 'second')

# 删除第 3 个位置的串.
lb.delete(3)


lbl.pack()
b.pack()
lb.pack()

window.mainloop()
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import tkinter as tk

window = tk.Tk()
window.geometry('200x200')

def hit_me():
	# 声明一个弹窗 messagebox. 其他的类型还有:
	#	showwarning
	#	showerror
	#	askquestion
	#	askyesno
	#	asktrycancel
	tk.messagebox.showinfo(title='Hit me', message='hahahah')

tk.Button(
		window,
		text='Click me',
		command=hit_me
	).pack()

window.mainloop()

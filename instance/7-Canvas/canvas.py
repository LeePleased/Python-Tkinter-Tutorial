# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import tkinter as tk


'''
显示画布, Canvas 可以用来画直线, 圆等.
'''

window = tk.Tk()
window.geometry('200x200')

# 创建一个 Canvas 对象.
canvas = tk.Canvas(
		window,
		bg='blue',
		height=100,
		width=200
	)
canvas.pack()

x0, y0, x1, y1 = 50, 50, 80, 80
line = canvas.create_line(x0-20, y0-20, x1+20, y1+20, width=5)
oval = canvas.create_oval(x0, y0, x1, y1, fill='yellow')
arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180)
rect = canvas.create_rectangle(100+50, 30, 150+20, 30+20)

def moveIt():
	# Canvas 内置的静态方法, 将对象移动 dx > 0,
	# dy > 0 步, 即 (dx, dy).
	canvas.move(rect, 0, 2)

b = tk.Button(
		window,
		text='move',
		width=20,
		command=moveIt
	)
b.pack()

window.mainloop()
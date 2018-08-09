# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import tkinter as tk
import tkinter.messagebox
import pickle


'''
显示一个用户登录界面.
'''

window = tk.Tk()
window.title('Welcome to LiePleased')
window.geometry('450x290')

# 加载 welcome 图像.
canvas = tk.Canvas(window, height=150, width=500)
# 似乎只能加载 gif 图片文件.
image_file = tk.PhotoImage(file='./photos/welcome.gif')
image = canvas.create_image(
		0, 0, 
		anchor='nw', 
		image=image_file
	)
canvas.pack(side='top')

# 用户信息标签.
tk.Label(window, text='User name:').place(x=50, y=150)
tk.Label(window, text='Password:').place(x=50, y=190)

var_usr_name = tk.StringVar()
var_usr_name.set('example@gmail.com')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name, width=30)
entry_usr_name.place(x=160, y=150)

var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*', width=30)
entry_usr_pwd.place(x=160, y=190)

# 定义事件响应函数.
def usr_login():
	usr_name = var_usr_name.get()
	usr_pwd = var_usr_pwd.get()

	try:
		with open('./database/usrs_info.pickle', 'rb') as usr_file:
			usrs_info = pickle.load(usr_file)
	except Exception:
		with open('./database/usrs_info.pickle', 'wb') as usr_file:
			usrs_info = {'admin': 'admin'}
			pickle.dump(usrs_info, usr_file)

	if usr_name in usrs_info.keys():
		if usr_pwd == usrs_info[usr_name]:
		 	tk.messagebox.showinfo(title='Welcome', message='How are you? ' + usr_name)
		else:
		 	tk.messagebox.showerror(message='Error, your password is wrong, try again.')
	else:
		is_sign_up = tk.messagebox.askyesno('Welcome', 'You have not sign up yet. sign up today?')
		if is_sign_up:
			usr_sign_up()

# 需要一个窗口上的窗口, Toplevel.
def usr_sign_up():
	def sign_to_email():
		np = new_pwd.get()
		npf = new_pwd_confirm.get()
		nn = new_name.get()

		with open('./database/usrs_info.pickle', 'rb') as usr_file:
			exist_usr_info = pickle.load(usr_file)

		if np != npf:
			tk.messagebox.showerror('Error', 'Passward and confirm passward must be the same.')
		elif nn in exist_usr_info:
			tk.messagebox.showerror('Error', 'The user has already signed up!')
		else:
			exist_usr_info[nn] = np
			with open('./database/usrs_info.pickle', 'wb') as usr_file:
				pickle.dump(exist_usr_info, usr_file)
			tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
			window_sign_up.destroy()

	window_sign_up = tk.Toplevel(window)
	window_sign_up.geometry('350x200')
	window_sign_up.title('Sign up window')

	new_name = tk.StringVar()
	new_name.set('example@gmail.com')
	tk.Label(window_sign_up, text='User name: ').place(x=10, y=10)
	entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
	entry_new_name.place(x=150, y=10)

	new_pwd = tk.StringVar()
	tk.Label(window_sign_up, text='Passward: ').place(x=10, y=50)
	entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
	entry_usr_pwd.place(x=150, y=50)

	new_pwd_confirm = tk.StringVar()
	tk.Label(window_sign_up, text='Confirm passward: ').place(x=10, y=90)
	entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
	entry_usr_pwd_confirm.place(x=150, y=90)

	btn_confirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_email)
	btn_confirm_sign_up.place(x=150, y=130)

# login 和 sign up 按钮.
btn_login = tk.Button(window, text='Login', command=usr_login, width=10)
btn_login.place(x=10, y=250)

btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up, width=10)
btn_sign_up.place(x=360, y=250)

window.mainloop()

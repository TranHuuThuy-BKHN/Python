from tkinter import *
class frame(Frame):
	def __init__(self, master = None, width = 400, height = 500, title = None):
		super().__init__(master)
		self.master.title(title)
		self.master.minsize(width, height)
		self.master.maxsize(width, height)
	def addLabel(self, string = None, x = 0, y = 0):
		lable = Label(self.master, textvariable = string, fg = 'black', font = 'Time 10')	
		lable.pack()
		lable.place(x = x, y = y)
	def addEntry(self, string = None, x = 0, y = 0, protected = False):
		if protected == False:
			entry = Entry(self.master, textvariable = string, bd = 2, width = 35)
		else : 	entry = Entry(self.master, textvariable = string, bd = 2, width = 35, show = '*')
		entry.pack()
		entry.place(x = x, y = y)	
	def addCheckButton(self, name = None, x = 0, y = 0):
		cb = Checkbutton(self.master, text = name)
		cb.pack()
		cb.place(x = x, y = y)
	def addButton(self, name = None, x = 0, y = 0, command = None):
		bt = Button(self.master, text = name, width = 30, command = command, height = 2, bg = 'pink', font = 'Time 9')
		bt.pack()
		bt.place(x = x, y = y)	
fr = frame(title = 'Garena')
title = Label(fr.master, text = 'Garena', fg = 'red', font = 'Time 20')
title.pack()
name = StringVar()
stringName = StringVar()
name.set('Your ID')
fr.addLabel(string = name , x = 60, y = 100)
fr.addEntry(string = stringName, x = 150, y = 100)
passWord = StringVar()
stringPass = StringVar()
passWord.set('Pass Word')
fr.addLabel(string = passWord , x = 60, y = 140)
fr.addEntry(string = stringPass, x = 150, y = 140, protected = True)
fr.addCheckButton(name = 'Nhớ mật khẩu', x = 150, y = 180)
fr.addButton(name = 'Đăng nhập', x = 150, y = 220)
fr.addButton(name = 'Tạo tài khoản', x = 150, y = 270)
fr.mainloop()	

from tkinter import *
class frame(Frame):
	def __init__(self, master = None, width = 400, height = 200, title = 'tkinter'):
		super().__init__(master)
		self.master.title(title)
		self.master.geometry(str(width) + 'x' + str(height) + "+400+250")
		self.master.maxsize(400, 400)
fr = frame(title = 'Entry')
string = StringVar()
en = Entry(fr.master, text = 'Your name', width = 15, font = 'Time', fg = 'red', textvariable = string)
en.pack()
def display():
	print('Ban nhap :', string.get())
def delete():
	en.select_clear()	
bt = Button(fr.master, text = 'display', width = 10, command = display)
bt.pack()
deButton = Button(fr.master, text = 'delete', width = 10, command = delete)
deButton.pack()
fr.mainloop()
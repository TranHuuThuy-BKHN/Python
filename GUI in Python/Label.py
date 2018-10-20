from tkinter import *
class frame(Frame):
	def __init__(self, master = None, width = 400, height = 200, title = 'Label'):
		super().__init__(master)
		self.master.title(title)
		self.master.minsize(width, height)
fr = frame()
string = StringVar()
label = Label(fr.master, textvariable = string)
string.set('Trần Hữu Thúy')
label.pack()
def change():
	string.set('Phan Thanh Phong')
bt = Button(fr.master, text = 'change', command = change)
bt.pack()
fr.mainloop()

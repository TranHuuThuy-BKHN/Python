from tkinter import *
class frame(Frame):
	def __init__(self, master = None, width = 300, heigth = 300):
		super().__init__(master)
		self.var = IntVar()
		self.master.title('program one')
		self.master.minsize(width, heigth)
	def hello(self):
		print('hello')	
fr = frame()	
fred = Button(fr.master, text = 'hello', activeforeground = 'red', fg = 'black', bg = 'white', command = fr.hello)	
fred.pack()
fred.place(x = 100, y = 100)
fred1 = Button(fr.master, text = 'exit', activeforeground = 'red', fg = 'black', bg = 'white', command = fr.quit)
fred1.pack(side = 'right')
fred1.place(x = 150, y = 100)
cb = Checkbutton(fr.master, text = 'check', variable =  fr.var, onvalue = 1, offvalue = 0, command = fr.hello)
cb.pack()
cb.place(x = 180, y = 100)
fr.mainloop()
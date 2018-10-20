from tkinter import *
class frame(Frame):
	def __init__(self, master = None, width = 400, height = 200):
		super().__init__(master)
		self.var = IntVar()
		self.var1 = IntVar()
		self.master.title('checkbutton')
		self.master.minsize(width, height)
		self.pack()
	def quit(self):
		if self.var.get() == 1:
			print('click on checkbutton')
		else :
			print("don't click")	
fr = frame()
cb = Checkbutton(fr, text = 'checkbutton', variable = fr.var, fg = 'red', onvalue = 1, offvalue = 0, command = fr.quit)
cb.config(fg = 'black', activeforeground = 'blue')
cb.pack()
cb1 = Checkbutton(fr, text = 'checkbutton', variable = fr.var1, fg = 'red', onvalue = 1, offvalue = 0, command = fr.quit)
cb1.config(fg = 'black', activeforeground = 'blue')
cb1.toggle()
cb1.pack(side = 'left')
fr.mainloop()		
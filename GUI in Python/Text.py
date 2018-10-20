from tkinter import *
class application(Frame):
	def __init__(self, master = None):
		super().__init__(master)
		self.config(width = 200, height = 100)
		self.pack()
	def creat_widget(self):
		self.text = Text(self, width = 10, height = 10).pack()
root = Tk()

app = application(master = root)
app.creat_widget()
app.mainloop()		

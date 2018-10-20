from tkinter import *
class frame(Frame):
	def __init__(self, master = None, width = 200, height = 200, title = None):
		super().__init__(master)
		self.master.title(title)
		self.master.minsize(width, height)
	def move(self, event):
		if event.keysym == 'Up':
			cv.move(1, 0, -2)
		elif event.keysym == 'Down':
			cv.move(1, 0, 2)
		elif event.keysym == 'Left':
			cv.move(1, -2, 0)
		else :
			cv.move(1, 2, 0)			
fr = frame(width = 400, height = 400, title = 'Canvas')	
cv = Canvas(fr.master, bg = 'gray', cursor = 'dot', width = 100, height = 100)
cv.pack()
cv.create_oval(20, 20, 50, 50, outline = 'red', fill = 'blue')
cv.create_text(40, 30 , text = 'Nghịch thôi', font = 'Time-10')
cv.bind_all('<KeyPress>', fr.move)
fr.mainloop()	
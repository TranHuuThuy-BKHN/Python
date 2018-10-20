from tkinter import *
from tkinter import ttk
import time


class Ball:
	def __init__(self):
		self.stateBall = 'down'
		self.ball = canvas.create_oval(10, 10, 30, 30, fill = 'red') 
	def move(self):
		if self.stateBall == 'down':
			canvas.move(self.ball, 0, 5)
			if canvas.coords(self.ball)[3] == 300:
				self.stateBall = 'up'

		else :
			canvas.move(self.ball, 0, -5)			
			if canvas.coords(self.ball)[1] == 0:
				self.stateBall = 'down'

root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()

b = Ball()

while True:
	b.move()
	time.sleep(0.03)
	root.update()
	
root.mainloop()
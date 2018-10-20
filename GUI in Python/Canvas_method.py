from tkinter import *
import datetime
import time
import calendar

class root(Frame):
	def __init__(self, master = None, width = 400, height = 400):
		super().__init__(master)
		self.master.minsize(width = width, height = height)
		self.master.resizable(0, 0)
		self.menu()
		self.pack()

		self.time = StringVar()
		tday = datetime.datetime.today()
		self.time.set(tday.strftime('%H:%M:%S'))

		Frame(self, width = width, height = 20).grid(row = 0, columnspan = 7)
		#điền cấc thứ
		car = calendar.month(tday.year, tday.month).split()
		for i in range(7):
			Label(self, text = car[i+2], font = 'Time 10').grid(row = 1, column = i, padx = 5, pady = 2)

		bday = datetime.date(tday.year, tday.month, 1)
		col = bday.weekday()
		r = 2
		#điền ngày
		for i in car[9:]:
			if int(i) == tday.day :
				i = i + '*'
				Label(self, text = i, font = 'Time 10', fg = 'red').grid(row = r, column = col, padx = 50, pady  =  2)
			else : Label(self, text = i, font = 'Time 10', fg = 'blue').grid(row = r, column = col, padx = 50, pady = 2)	
			if col > 6 : col = -1 
			if col == 6: 
				r += 1
				col = -1
			col +=1	

		Label(self, text = car[0] + ' ' + car[1], font = 'Time 15', fg = 'red').grid(column = 3, sticky = 'sn')	
		#vẽ đồng hồ
		self.canvas = Canvas(self, width = 100, height = 100)
		self.canvas.grid(column = 1, padx = 10, pady = 30, sticky = 'n')
		oval = self.canvas.create_oval(5, 5, 95, 95)

	def menu(self):
		w = Menu(self.master, tearoff = 0)
		w.add_command(label = 'calendar', command = self.newCalendar)
		w.add_command(label = 'add member', command = self.newAdd)
		self.master.config(menu = w)

	def calendar(self):
		pass	
	
	def add(self):
		pass

	def newCalendar(self):
		self.calendar()

	def newAdd(self):
		self.add()
		

master = Tk()
master.title('Lịch sinh nhật')
root = root(master = master)
root.mainloop()					
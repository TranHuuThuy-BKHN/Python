from tkinter import *
from tkinter import ttk
import datetime
import calendar


class root(Frame):
	def __init__(self, master = None):
		super().__init__(master)
		self.master.resizable(0, 0)
		self.list = {}
		self.readFile()
		self.initGUI()

	def readFile(self):
		self.list = {}
		f = open('birthday.txt', 'r')
		today = datetime.date.today()
		for line in f:
			lis = (line.rstrip('\n')).split('/')
			time = datetime.date(today.year, int(lis[2]), int(lis[1]))
			if time >= today : 
				self.list[lis[0]] = time - today
		f.close()

	def initGUI(self):

		menu = Menu(self.master, tearoff = 0)
		menu.add_command(label = 'List member')
		menu.add_command(label = 'Add member', command = self.addMember)
		self.master.config(menu = menu)	

		for i in range(10):
			self.master.rowconfigure(i, weight = 50)
			self.master.columnconfigure(i, weight = 50)

		style = ttk.Style()
		style.configure('header.TLabel', foreground = 'blue', font = 'Time 20 bold')	
		ttk.Label(self.master, text = 'CALENDAR',
				 style = 'header.TLabel').grid(row = 0, column = 4, columnspan = 3)	

		today = datetime.datetime.today()
		cal = calendar.month(today.year, today.month).split()

		style2 = ttk.Style()
		style2.configure('cal.TLabel', foreground = 'green', font = 'Time 10')
		for i in range(7):
			ttk.Label(self.master, text = cal[i + 2],
					 style = 'cal.TLabel').grid(row = 1, column = i+2, padx = 10)

		fistMonth = datetime.date(today.year, today.month, 1)
		col = fistMonth.weekday() + 2
		row = 2	

		for i in cal[9:]:
			if int(i) == today.day: 
				i = i + "*"
				ttk.Label(self.master, text = i, foreground = 'red').grid(row = row, column = col, padx = 10)
			else :	ttk.Label(self.master, text = i).grid(row = row, column = col, padx = 10)
			col += 1
			if col == 9:
				col = 2
				row += 1	

		ttk.Label(self.master, text = cal[0] + ' ' +cal[1], font = 'Time 10 bold').grid(row = 7, column = 3)

		time = today.strftime('%H:%M:%S')
		self.var = StringVar()
		self.var.set(time)
		Label(self.master, textvariable = self.var, font = 'Time 10 bold').grid(row = 7, column = 6)

		label = ttk.Label(self.master, font = 'Time 10', text = 'Từ giờ đến cuối năm không phải chờ sing nhật ai cả',
			             foreground = 'blue', wraplength = 300)
		label.grid(row = 8, column = 1, columnspan = 8, pady = 15)
		if len(self.list) :
			min_time = min(self.list.values())
			string = ''
			for i in self.list:
				if self.list[i] == min_time:
					string += i + ','
			if min_time : label.config(text = 'Sinh nhật ' + string + ' còn ' +str(min_time))
			else : 	label.config(text = 'Hôm nay là sinh nhât của ' + string)
		while True:
			if len(self.list) :
				min_time = min(self.list.values())
				string = ''
				for i in self.list:
					if self.list[i] == min_time:
						string += i + ','
				if min_time : label.config(text = 'Sinh nhật ' + string + ' còn ' +str(min_time))
				else : 	label.config(text = 'Hôm nay là sinh nhât của ' + string)

			self.var.set(datetime.datetime.today().strftime('%H:%M:%S'))
			self.master.update()

	def addMember(self):
		window = Toplevel(self.master)
		window.title('add member')
		window.geometry('300x200+500+250')
		window.resizable(0, 0)

		for i in range(10):
			window.rowconfigure(i, weight = 20)
			window.columnconfigure(i, weight = 25)
		style3 = ttk.Style()
		style3.configure('W.TLabel', foreground = 'blue')

		ttk.Label(window, text = 'Name', style = 'W.TLabel').grid(row = 1, column = 1, sticky = 'se', pady = 2)	
		ttk.Label(window, text = 'Birdthday', style = 'W.TLabel').grid(row = 2, column = 1, sticky = 'ne', pady = 2)

		self.name = StringVar()
		self.birdthday = StringVar()

		self.NAME = ttk.Entry(window, textvariable = self.name,
							 width  = 30).grid(row = 1, column = 2, sticky = 'se', pady = 2)
		self.BD = ttk.Entry(window, textvariable = self.birdthday,
							 width  = 30).grid(row = 2, column = 2, sticky = 'ne', pady = 2)

		def add():
			li = self.birdthday.get().split('/')
			time = datetime.date(int(li[2]), int(li[1]), int(li[0]))

			f = open('birthday.txt', 'a')
			f.write(self.name.get() + '/' +self.birdthday.get() + f'\n')
			f.close()

			self.readFile()

			self.name.set('')
			self.birdthday.set('')

		def exit():
			window.destroy()	

		ttk.Button(window, text = 'exit', width = 10
			, command = exit).grid(row = 3, column = 2, sticky = 'e', padx = 5)
		ttk.Button(window, text = 'add', width = 10
			, command = add).grid(row = 3, column = 2, padx = 5, sticky = 'w')
		
master = Tk()
master.minsize(250, 300)
master.title('Lịch sinh nhật')
Root = root(master = master)

Root.mainloop()
from tkinter import *
class application(Frame):
	def __init__(self, master = None):
		super().__init__(master)
		self.master.resizable(width = FALSE, height = FALSE)
		self.master.minsize(width = 400, height = 500)
		self.config(width = 400, height = 500)
		self.pack()

	def creat_widget(self):
		
		self.label = Label(self, text = 'Thông tin sinh viên Bách Khoa', fg = 'blue', font = 'Time 18')
		self.label.pack()
		self.listbox = Listbox(self, width = 60, height = 15)
		self.scrollbar = Scrollbar(self, width = 15, command = self.listbox.yview)
		self.listbox.config(yscrollcommand = self.scrollbar.set)
		for i in range(1000):
			self.listbox.insert(END, i)
		self.listbox.pack(side = 'left', fill =  Y)
		self.scrollbar.pack(side = 'left', fill = Y)

		self.name = StringVar()
		self.msv = StringVar()
		self.sdt = StringVar()

		Label(self.master, text = 'Tên sinh viên').place(x = 15, y = 300)
		Entry(self.master, textvariable = self.name, width = 35, bd = 2).place(x = 100, y = 300)

		Label(self.master, text = 'Mã sinh viên').place(x = 15, y = 330)
		Entry(self.master, textvariable = self.msv, width = 35, bd = 2).place(x = 100, y = 330)

		Label(self.master, text = 'Số điện thoại').place(x = 15, y = 360)
		Entry(self.master, textvariable = self.sdt, width = 35, bd = 2).place(x = 100, y = 360)

root = Tk()
root.title('application')
app = application(master = root)
app.creat_widget()	
app.mainloop()
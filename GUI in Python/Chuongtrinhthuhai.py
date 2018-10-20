#chương trình hiển thị giao diện quản lý thông tin sinh viên

from tkinter import *

root = Tk()
root.minsize(width = 700, height = 400)
root.title('Quản lý sinh viên')
root.resizable(width = FALSE, height = FALSE)
class informationStudent:
	def __init__(self, width = 700, height = 400):
		fr = Frame(root, width = width, height = height)
		Label(fr, text = 'THÔNG TIN SINH VIÊN', font = 'Time 20', fg = 'red').pack()
		sc = Scrollbar(fr, width = 12)
		lb = Listbox(fr, width = 100, height = 20, yscrollcommand = sc.set)
		for i in range(1000):
			lb.insert(END, 'I am ' + str(i))
		sc.config(command = lb.yview)
		sc.pack(side = 'right', fill = Y)
		lb.pack(side = 'right', fill = Y)
		fr.pack()

class addStudent:
	def __init__(self, width = 700, height = 400):
		pass
	def addSt(self):
		pass	



class deleteStudent:
	def __init__(self, width = 700, height = 400):
		pass

	def delete(self):
		pass

class findStudent:
	def __init__(self, width = 700, height = 400):
		pass
		
	def find(self):
		pass	


def display_addStudent():
	disphay = addStudent()

def display_deleteStudent():
	disphay = deleteStudent()

def disphay_findStudent():
	disphay = findStudent()	

def disphay_student():
	disphay = informationStudent()

#menu làm việc có ba giao thức, hiện thị thông tin sinh viên, thêm sinh viên, xóa thông tin sinh viên, tìm sinh viên
menu = Menu(root, tearoff = 0)

menu.add_command(label = 'Thông tin sinh viên', command = disphay_student)
menu.add_command(label = 'Thêm sinh viên', command = display_addStudent)
menu.add_command(label = 'Xóa thông tin sinh viên', command = display_deleteStudent)
menu.add_command(label = 'Tìm sinh viên', command = disphay_findStudent)

root.config(menu = menu)

root.mainloop()
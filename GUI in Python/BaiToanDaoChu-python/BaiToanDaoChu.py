#hai chuỗi gọi là đảo của nhau nếu có chung tập kí tự chữ cái, không quan tâm đến khoảng trắng và viết hoa hay thường

#=====Giải thuật 1 checkoff====
#hàm xóa khoảng trắng và viết hoa
def freeSpaceUpper(string):
	lis = string.split()
	string = ''
	for i in lis:
		string += i.upper()
	return string

def algorithm1(str1, str2):
	str1 = freeSpaceUpper(str1)
	str2 = freeSpaceUpper(str2)
	if len(str1) != len(str2): return False
	#Tạo mảng checkoff
	checkOff = [0 for i in str1]

	list1 = [i for i in str1]
	list2 = [i for i in str1]

	for i in range(len(list1)):
		for j in range(len(list2)):
			if list1[i] == list2[j] and checkOff[j] == 0:
				checkOff[j] = 1
				break

	if 0 in checkOff: return False
	return True			
#==============Giải thuật 2 - sắp xếp ==============
def algorithm2(str1, str2):
	str1 = freeSpaceUpper(str1)
	str2 = freeSpaceUpper(str2)
	#danh sách chứa các kí của hai chuỗi
	lis1 = [i for i in str1]
	lis2 = [i for i in str2]
	lis1.sort()
	lis2.sort()
	if lis1 == lis2: return True
	return False

#Giải thuật 3 là vét cạn nên mình không muốn làm

#Đoạn này là do mình không biết làm thế nào để tạo ra nên mình viết hết luôn
l = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def algorithm4(str1, str2):
	str1 = str1.upper()
	str2 = str2.upper()
	lis1 = []
	lis2 = []
	for char in l:
		lis1.append(str1.count(char))
		lis2.append(str2.count(char))
	if lis1 == lis2 : return True
	return False

from tkinter import *

root = Tk()
root.minsize(width = 500, height = 500)
root.title('Sublect 1')
root.resizable(width = FALSE, height = FALSE)
frame = Frame(root, height = 80,width = 500).grid(row = 0, columnspan = 3)
#Đặt tên cho bài toán
Label(frame, text = 'Bài Toán Đảo Chữ', font = 'Time 30', fg = 'red').grid(row = 0, column = 1, sticky = 'w')

#tạo nơi nhập hai chuỗi
str1 = StringVar()
str2 = StringVar()
value = IntVar()
value.set(4)

Label(root, text  = 'Chuỗi 1', fg = 'black', font = 'Time 12').grid(row = 1, column = 0, sticky = 'e')
Entry(root, textvariable = str1, width = 40, bd = 2, font = 'Time 10').grid(row = 1, column = 1)

Frame(root, height = 10,width = 500).grid(row = 2, columnspan = 3)

Label(root, text  = 'Chuỗi 2', fg = 'black', font = 'Time 12').grid(row = 3, column = 0, sticky = 'e')
Entry(root, textvariable = str2, width = 40, bd = 2, font = 'Time 10').grid(row = 3, column = 1, sticky = '')

Frame(root, width = 500, height = 30).grid(row = 4, columnspan = 10)
#Nơi lựa chọn giải thuật
algorithm = StringVar()
algorithm.set('algorithm 1')
OptionMenu(root, algorithm, 'algorithm 1', 'algorithm 2', 'algorithm 3', 'algorithm 4', 'all algorithm').grid(row = 5, column = 1)

#hiển thị cái gì
value1 = StringVar()
value1.set('Kết quả')
OptionMenu(root, value1, 'Thời gian', 'Kết quả', 'Thời gian+kết quả').grid(row = 6, column = 1)

Frame(root, width = 500, height = 150).grid(row = 7, columnspan = 3)
#dữ liệu được sinh ngẫu nhiên
def randomData():
	pass
var = IntVar()
var.set(0)
cb = Checkbutton(root, text = 'Sinh dữ liệu', variable = var, onvalue = 1, offvalue = 0, command = randomData, font = 'Time 12')
cb.grid(row = 8, column = 0)

def runAlgorithm(fr):
	result = True
	if value.get() == 1: result = algorithm1(str1.get(), str2.get())
	elif value.get() == 2 : result = algorithm2(str1.get(), str2.get())
	else : result = algorithm4(str1.get(), str2.get())
	lb = Label(fr, text = 'Kết quả giải thuật '+ repr(value.get()) + ' là '+ repr(result), font = 'Time 12', fg = 'red')
	lb.grid(row = 7, column = 1)
#hai nút bấm ran và exit
def Run():
	if var.get() == 1: 
		randomData()
		fr = Frame(root, width = 500, height = 150).grid(row = 7, columnspan = 3)
		runAlgorithm(fr)
	else :
		if len(str1.get()) * len(str2.get()) == 0:
			fr = Frame(root, width = 500, height = 150).grid(row = 7, columnspan = 3)
			lb = Label(fr, text  = 'Chưa có dữ liệu', fg = 'red', font = 'Time 12').grid(row = 7, column = 1)
		else : 
			fr = Frame(root, width = 500, height = 150).grid(row = 7, columnspan = 3)
			runAlgorithm(fr)


		
run = Button(root, text = 'Run', width = 10, bd = 4, command = Run, font = 'Time 10', fg = 'blue').grid(row = 8, column = 1, sticky = 'e')
exit = Button(root, text = 'Exit', width = 10, bd = 4, command = root.quit, font = 'Time 10', fg = 'blue').grid(row = 8, column = 2, sticky = 's')

root.mainloop()
from tkinter import *
from tkinter import ttk

#du lieu ban dau
f = open('data.txt')
data = []
for line in f:
	tup = tuple(line.split(','))
	data.append(tup)

def cmp_name(tup):
	lis = tup[0].split()
	return lis[-1]

data.sort(key = cmp_name)
#===========================================

root = Tk()
root.title('Sinh Viên Bách Khoa')
root.resizable(0,0)

#tao cac note book
notebook = ttk.Notebook(root)
notebook.pack()

style = ttk.Style()
style.configure('F.TFrame', background = 'pink')

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook, style = 'F.TFrame')
frame3 = ttk.Frame(notebook, width = 600, height = 300)
notebook.add(frame1, text = 'Thông tin sinh viên')
notebook.add(frame2, text = 'Thêm sinh viên')
notebook.add(frame3, text = 'Tìm sinh viên')
#=========================================

#=====Frame1===========================
ttk.Label(frame1, text = 'Danh sách thông tin sinh viên', 
		font = 'Time 20 bold', foreground = 'blue').pack(pady = 5)
scrollbar = Scrollbar(frame1, width = 12)
listbox = Listbox(frame1, width = 100, height = 15, yscrollcommand = scrollbar.set)
listbox.pack(side = 'left', fill = Y, padx = 5, pady = 5)
#======Lay du lieu ban dau======	
scrollbar.config(command = listbox.yview)
scrollbar.pack(side = 'left', fill = Y)
#===============Frame2============================

frame11 = ttk.Frame(frame2, width = 300, height = 300, relief = RIDGE)
frame11.grid(row = 0, column = 0, padx = 20, pady = 10)
frame12 = ttk.Frame(frame2, width = 300, height = 300)
frame12.grid(row = 0, column = 1)
	#anh nen cho fram11
logo = PhotoImage(file = 'bachkhoa.png').subsample(4, 3)
ttk.Label(frame11, image = logo, text = 'BK in my heart', 
		compound = 'top', font = 'Arial 10 bold').pack()
	#tao frame12
name = StringVar()
msv = StringVar()
lop = StringVar()
sdt = StringVar()

ttk.Label(frame12, text = 'Họ tên').grid(row = 0, column = 0, padx = 10, pady = 10)
ttk.Entry(frame12, textvariable = name, width = 35).grid(row = 0, column = 1, padx = 10, pady = 10)
ttk.Label(frame12, text = 'Msv').grid(row = 1, column = 0,  padx = 10, pady = 20)
ttk.Entry(frame12, textvariable = msv, width = 35).grid(row = 1, column = 1, padx = 10, pady = 10)
ttk.Label(frame12, text = 'Lớp').grid(row = 2, column = 0,  padx = 10, pady = 20)
ttk.Entry(frame12, textvariable = lop, width = 35).grid(row = 2, column = 1, padx = 10, pady = 10)
ttk.Label(frame12, text = 'Sdt').grid(row = 3, column = 0,  padx = 10, pady = 20)
ttk.Entry(frame12, textvariable = sdt, width = 35).grid(row = 3, column = 1, padx = 10, pady = 10)

add = ttk.Button(frame12, text = 'add', width = 10, state = 'disabled')
add.grid(row = 4, column = 1)
#=======================Frame3=====================================
frame31 = ttk.Frame(frame3, width = 600, height = 100)
frame31.pack()
frame32 = ttk.LabelFrame(frame3, width = 600, height = 200, text = 'Kết quả tìm kiếm')
frame32.pack()

inf = StringVar()
ttk.Label(frame31, text = 'Thông tin tìm kiếm').grid(row = 0, column = 0, padx = 5, pady = 10)
ttk.Entry(frame31, width = 35, textvariable = inf).grid(row = 0, column = 1)
sel = StringVar()
sel.set('Họ và tên')
value = ('Họ và tên', 'Mã sinh viên', 'Lớp', 'Số điện thoại')
ttk.Combobox(frame31, textvariable = sel, values = value, state = 'readonly',
			 justify = 'center').grid(row = 0, column = 2, padx = 5)
#ham kiem tra xem str1 co phai la tien to cua str2 hay khong
def check():
	for sv in data:
		if inf in sv[0]:
			pass
find = ttk.Button(frame31, text = 'Tìm kiếm', width = 20, state = 'disabled')
find.grid(row = 1, column = 1)
ttk.Button(frame31, text = 'Xóa', width = 20).grid(row = 1, column = 2)

scroll = Scrollbar(frame32, width = 12)
scroll.pack(side = 'right', fill = Y, pady = 10)
listResult = Listbox(frame32, width = 90, height = 10, yscrollcommand = scroll.set)
listResult.pack(fill = Y, side = 'right', pady = 10)
scroll.config(command = listResult.yview)
	
while True:
	if inf.get():find.config(state = 'normal')
	else : find.config(state = 'disabled')
	if name.get() and msv.get() and lop.get() and sdt.get():
		add.config(state = 'normal')
	else : add.config(state = 'disabled')	
	root.update()
	
root.mainloop()		

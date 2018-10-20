from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Thanh Toán Tiền Ăn')
root.configure(background = 'brown')

#=====Combobox==========
typeFood = StringVar()
typeFood.set('Nước uống')
value = ('Nước uống', 'Hải sản', 'Hoa quả', 'Lẩu')
ttk.Combobox(root, textvariable = typeFood, values = value, 
			state = 'readonly', justify = 'center', width = 12).grid(pady = 5)

#=====Listbox_1=========
listOne = Listbox(root, width = 40, height = 20, relief = RIDGE)
logo = PhotoImage(file = 'AnhNen.png').subsample(40, 40)
for i in range(100):
	listOne.insert(i, 'hello' + repr(i))
listOne.grid(row = 1, column = 0, padx = 10, pady = 5)
scrollbarOne = Scrollbar(listOne, command = listOne.yview, width = 12)
scrollbarOne.pack(side = 'right', fill = Y)
listOne.config(yscrollcommand = scrollbarOne.set)

#=====Listbox_2
listTwo = Listbox(root, width = 40, height = 15, relief = RIDGE)
listTwo.grid(row = 1, column = 1, padx = 10, pady = 7, sticky = 'n')

root.mainloop()
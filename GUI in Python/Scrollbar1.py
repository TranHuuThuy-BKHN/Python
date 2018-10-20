from tkinter import *

root = Tk()

root.minsize(width = 200, height = 200)
f = Frame(root, width = 200, height = 30)
k = Label(f, text = 'Xin Chao').pack()
f.pack()
sc = Scrollbar(root, width = 10)
li = Listbox(root, width = 40, height = 10, yscrollcommand = sc.set)
for i in range(100):
	li.insert(END, i)
sc.config(command = li.yview)
sc.pack(side = 'right', fill = Y)
li.pack( fill = Y)
root.mainloop()
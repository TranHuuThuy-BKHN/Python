from tkinter import *
from tkinter import ttk

root = Tk()

root.minsize(400, 400)
for i in range(8):
	root.rowconfigure(i, weight = 50)
	root.columnconfigure(i, weight = 50)

style = ttk.Style()
style.configure('1.TFrame', )

ttk.Frame(root, style = '1.TFrame', relief = RIDGE, 
			width = 200, height = 400).grid(row = 3, column = 1, sticky = 'n')

root.mainloop()
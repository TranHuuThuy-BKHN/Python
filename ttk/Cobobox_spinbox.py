from tkinter import *
from tkinter import ttk

master = Tk()
var = StringVar()
var.set('one')
combobox = ttk.Combobox(master, textvariable = var)
combobox.config(values = ('one', 'two', 'three', 'four', 'five', 'six'))
combobox.pack()
year = StringVar()
spinbox = Spinbox(master, textvariable = year, from_ = 1980, to = 2020)
spinbox.pack(padx = 10, pady = 20)
master.mainloop()
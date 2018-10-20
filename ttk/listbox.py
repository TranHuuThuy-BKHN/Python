from tkinter import *
from tkinter import ttk

master = Tk()
master.minsize(500, 300)
lisbox = Listbox(master, width = 50, height = 10, selectmode = EXTENDED)
lisbox.pack()
img = PhotoImage(file = 'AnhNen.png').subsample(50, 50)
for i in range(10):
	la = ttk.Label(master, image = img)
	lisbox.insert(END, la)
master.mainloop()
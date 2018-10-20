from tkinter import *
from tkinter import ttk

master = Tk()
lb = ttk.Label(master, text = 'I am a label')
lb.pack()

style = ttk.Style()
style.configure('TLabel', foreground = 'blue')
lb.config(style = 'TLabel')

lb2 = ttk.Label(master, text = 'I am a label')
lb2.pack()

logo = PhotoImage(file = 'AnhNen.png').subsample(40, 40)
lb2.config(image = logo, compound = LEFT, wraplength = 50, justify = 'center')
master.mainloop()
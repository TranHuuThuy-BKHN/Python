from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.title('progressbar')

value = IntVar()
prog = ttk.Progressbar(root)
prog.start(interval = 60)
prog.pack()
root.mainloop()
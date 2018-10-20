from tkinter import *
from tkinter import ttk

root = Tk()
notebook = ttk.Notebook(root)
notebook.pack()
fr = ttk.Frame(notebook)
notebook.add(fr, text = 'hello')
fr2 = ttk.Frame(notebook)
notebook.add(fr2, text  = 'bye')
logo = PhotoImage(file = 'bachkhoa.png').subsample(4, 4)

frame = ttk.Frame(fr, width = 200, height = 200, relief = RIDGE)
frame.grid(row = 0, column = 0)

frame2 = ttk.Frame(fr, width = 200, height = 200, relief = RIDGE)
frame2.grid(row = 0, column = 1)

lb = ttk.Label(frame, image = logo)
lb.pack()
ttk.Button(frame2, text = 'button').pack()
root.mainloop()
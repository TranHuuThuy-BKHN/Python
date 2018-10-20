from tkinter import *
from tkinter import ttk
import datetime

master = Tk()
notebook = ttk.Notebook(master)
notebook.pack()

fram1 = ttk.Frame(notebook)
fram2 = ttk.Frame(notebook, width = 200, height = 200)
notebook.add(fram1, text = 'one')
notebook.add(fram2, text = 'two')

style = ttk.Style()
style.configure('B.TButton', foreground = 'blue', width = 10)

ttk.Button(fram1, text = 'click me', style = 'B.TButton').pack()

fram3 = ttk.Frame(notebook)
notebook.insert(1,fram3, text = 'three')
time = StringVar()

time.set(datetime.datetime.today().strftime('%H:%M:%S'))
label = ttk.Label(fram3, textvariable = time)
label.pack()
while True:
	time.set(datetime.datetime.today().strftime('%H:%M:%S'))
	master.update()
master.mainloop()

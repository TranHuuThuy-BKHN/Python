from tkinter import ttk
from tkinter import *

master = Tk()
master.configure(background = 'blue')
styl = ttk.Style()
styl.configure('Header.TLabel', foreground = 'red', font = {'Time' , 10, 'bold'}, background = 'brown')
button = ttk.Label(master, text = 'click me', style  = 'Header.TLabel')
button.config(style = 'TLabel')
button.pack()
def hello():
	print('Heloo tkinter')
button.state(['!disabled'])
logo = PhotoImage(file = 'AnhNen.png').subsample(60, 60)
button.config(image = logo, compound = LEFT)
fr = ttk.Frame(master, height = 50, width = 100)
st = ttk.Style()
st.configure('Tail.TFame',background = 'red')
fr.config(style = 'Tail.TFrame')
fr.pack()
label = ttk.Label(fr, text = 'hello', image = logo)
label.config(compound = RIGHT)
label.pack()
master.mainloop()

from tkinter import *
 
root = Tk()
root.minsize(width  = 300, height = 200)

fr = Frame(root, width = 300, height = 50).grid(row = 0, columnspan = 10)
Label(fr, text = 'Scale', font = 'Time 20', fg = 'red').grid(row = 0, column = 5, sticky = 'w')

var = IntVar()

def change(k = 0):
	pass

sc = Scale(root, from_ = 0, to = 50, label = 'value', font = 'Time 10', variable = var, command = change).grid(row = 1, column = 2, sticky = 'w')

root.mainloop()
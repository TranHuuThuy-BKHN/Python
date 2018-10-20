from tkinter import *

root = Tk()

root.minsize(width = 400, height = 100)

nameButton = StringVar()
nameButton.set('selectAlgorithm')
def re():
	nameButton.set('algorithm 1')

mb = Menubutton(root, textvariable = nameButton)
mb.grid()
mb.menu = Menu(mb, tearoff = 0)
mb['menu'] = mb.menu
mb.menu.add_command(label = 'algorithm 1', command = re)
root.mainloop()
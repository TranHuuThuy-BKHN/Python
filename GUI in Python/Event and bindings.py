from tkinter import *

root = Tk()

def key(event):
    if event.keysym == 'Up':
    	print('Up')
    elif event.keysym == 'Down':
    	print('Down')
    elif event.keysym == 'Left':
    	print('Left')	
    elif event.keysym == 'Right':
    	print('Right')	
    else:
    	print(event.keysym)			

frame = Frame(root, width=100, height=100)
frame.bind_all("<Key>", key)
frame.pack()

root.mainloop()
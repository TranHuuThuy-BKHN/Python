from tkinter import *
root = Tk()
root.minsize(width  = 200, height = 100)

scrollbar = Scrollbar(root, width = 12)
scrollbar.pack(side = 'right', fill= Y)
scrollbar1 = Scrollbar(root, width = 12, orient = HORIZONTAL)
scrollbar1.pack(side = 'bottom', fill = X)

lis = Listbox(root, yscrollcommand = scrollbar.set, xscrollcommand = scrollbar1.set)
for i in range(100):
	lis.insert(END, 'babjhsdjshdhdhdkahdakdkadkahdkjdkadhkadhdkahdkjhsadkahkd')
lis.pack( fill = BOTH)	
scrollbar.config(command = lis.yview)	
scrollbar1.config(command = lis.xview)
mainloop()
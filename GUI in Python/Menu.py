from tkinter import *
root = Tk()
root.title('Menu')
root.minsize(width = 400, height = 300)
root.resizable(width = FALSE, height = FALSE)

menu = Menu(root, tearoff = 0)

File = Menu(menu, tearoff = 0)
File.add_command(label = 'New File')
File.add_command(label = 'Open File')
File.add_command(label = 'Open Folder')
menu.add_cascade(label = 'File', menu = File)

Edit = Menu(menu, tearoff = 0)
Edit.add_command(label = 'Copy')
Edit.add_command(label = 'Cut')
Edit.add_command(label = 'Paste')
menu.add_cascade(label = 'Edit', menu = Edit)

root.config(menu = menu)
root.mainloop()
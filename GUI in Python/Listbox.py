from tkinter import *
root = Tk()
root.title('Grid')
root.minsize(300, 500)
root.resizable(height = FALSE, width = FALSE)
frame = Frame(root, width = 400, height = 50).grid(row = 0, columnspan = 5)
label = Label(frame, text = 'Garena',fg = 'red', font = 'Time 20').grid(row = 0, column = 2, sticky = 'nw')
label1 = Label(root, text = 'Username', fg = 'black', font = 'Time 10').grid(row = 1, column  = 1, sticky = 'w')
name = StringVar()
name.set('huuthuy2000@gmail.com')
entry = Entry(root, bd = 2, width = 30, textvariable = name).grid(row = 1, column = 2, sticky = 'w')
label2 = Label(root, text = 'Password', fg = 'black', font = 'Time 10').grid(row = 2 , column = 1, sticky = 'sw')
pas = StringVar()
pas.set('tranhuuthuy')
entry1 = Entry(root, bd = 2, width = 30, show = '*', textvariable = pas).grid(row = 2, column = 2, sticky = 'sw')
def save():
	if var.get() == 0:
		pas.set('')
	else :
		pas.set('tranhuuthuy')
var = IntVar()
cb = Checkbutton(root, text = 'Nhớ mật khẩu', variable = var, onvalue = 1, offvalue = 0, fg = 'black', command = save)
cb.select()
cb.grid(row = 3, column = 2, sticky = 'w')
bt = Button(root, text = 'Đăng nhập', bg = 'pink', fg = 'black', font = 'Time 10', width = 22).grid(row = 4, column = 2, sticky = 'w')
bt1 = Button(root, text = 'Tạo tài khoản', bg = 'pink', fg = 'black', font = 'Time 10', width = 22).grid(row = 5, column = 2, sticky = 'w')
root.mainloop()
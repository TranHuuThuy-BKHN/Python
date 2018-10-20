from tkinter import *
from tkinter import ttk
from math import *

lis = []
#ham giải phương trình bậc 2 và để nghiệm vào lis
def ptb2(a, b, c, lis):
	lis.clear()
	if a == 0:
		if b != 0: lis.append(- c / b)
	else : 
		delta = b * b - 4 * a * c
		if delta >= 0:
			x1 = (-b - sqrt(delta)) / (2 * a)
			x2 = (-b + sqrt(delta)) / (2 * a)	
			lis.append(x1)
			lis.append(x2)

master = Tk()
master.title('Giải phương trình bậc 2')
master.minsize(350, 250)
master.resizable(0, 0)
style = ttk.Style()

lbFrame = ttk.LabelFrame(master, text = 'Nhập hệ số a, b, c', width = 400, height = 150)
lbFrame.pack(pady = 20)

a = DoubleVar()
b = DoubleVar()
c = DoubleVar()

ttk.Label(lbFrame, text = 'Nhập a').grid(row = 0, column = 0, padx = 10, pady = 10)
ttk.Entry(lbFrame, textvariable = a, width = 25).grid(row = 0, column = 1, padx = 20, pady = 10)

ttk.Label(lbFrame, text = 'Nhập b').grid(row = 1, column = 0, padx = 10, pady = 10)
ttk.Entry(lbFrame, textvariable = b, width = 25).grid(row = 1, column = 1, padx = 20, pady = 10)

ttk.Label(lbFrame, text = 'Nhập c').grid(row = 3, column = 0, padx = 10, pady = 10)
ttk.Entry(lbFrame, textvariable = c, width = 25).grid(row = 3, column = 1, padx = 20, pady = 10)

lbFrame2 = ttk.LabelFrame(master, text = 'Result', width = 250, height = 50)
lbFrame2.pack()
result = StringVar()

lb = ttk.Label(lbFrame2, textvariable = result, width = 50, wraplength = 300)
lb.pack()

def run():
	if a.get() == 0 and b.get() == 0 and c.get() == 0:
		result.set('Phương trình có vô số nghiệm')
		return
	ptb2(a.get(), b.get(), c.get(), lis)
	if len(lis) == 1 or (len(lis) == 2 and lis[0] == lis[1]):
		result.set('Phương trình có nghiệm duy nhất x = %.3f' %lis[0] )
	elif len(lis) == 0:
		result.set('Phương trình vô nghiệm')
	else :	 	
		result.set('PT có 2 nghiệm phân biệt x1 = %.3f, x2 = %.3f' %(lis[0], lis[1])) 

ttk.Button(master, text = 'Exit', width = 10, command = master.destroy).pack(side = 'right', padx = 5, pady = 10)
ttk.Button(master, text = 'Run', width = 10, command = run).pack(side = 'right', padx = 5, pady = 10)

master.mainloop()
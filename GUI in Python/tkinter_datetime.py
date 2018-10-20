from tkinter import *
import datetime
import calendar

root = Tk()
root.title('Watch')
root.resizable(width = FALSE, height = FALSE)
root.minsize(height = 300, width = 300)
tg = datetime.datetime.today().strftime('%H:%M:%S')
time = StringVar()
car = StringVar()
car.set(calendar.month(2018,5))
time.set(tg)
label  = Label(root, textvariable = time, fg = 'black', font = 'Time 20').pack()
label2 = Label(root, textvariable = car).pack(pady = 3, side = 'left')
def change():
  car.set('name')
Button(root, text = 'bt', command = change).pack(side = 'right')
root.update()
while True:
  tg  = datetime.datetime.today().strftime('%H:%M:%S')
  time.set(tg)
  root.update()
root.mainloop()
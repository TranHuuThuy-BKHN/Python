from tkinter import *

root = Tk()

listBox = Listbox(root)
listBox.pack()

listOfCompanies = [[1, ''], [2, '-'], [3, '@ASK TRAINING PTE. LTD.'], [4, 'AAIS'], [5, 'Ademco'], [6, 'Anacle']]

def populatebox():
    for i in listOfCompanies:
        listBox.insert("end", i)

btn = Button(root, text="Update list", command = lambda: populatebox())
btn.pack()
root.mainloop()
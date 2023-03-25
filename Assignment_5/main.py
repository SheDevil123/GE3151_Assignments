from tkinter import *
import csv 


master = Tk()
def display_text():
   global e1,e2,e3,e4,e5,e6,e7,e8,e9
   data=e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get()
   with open("Assignment_5/data.csv", 'a') as f:
      f=csv.writer(f)
      f.writerow(data)
Label(master, text='First Name').grid(row=0)
Label(master, text='Last Name').grid(row=1)
Label(master, text='Address').grid(row=2)
Label(master, text='Blood group').grid(row=3)
Label(master, text='Weight').grid(row=4)
Label(master, text='Age').grid(row=5)
Label(master, text='Alcohol(Y/N)').grid(row=6)
Label(master, text='Drugs(Y/N)').grid(row=7)
Label(master, text='Smoking(Y/N)').grid(row=8)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)
e7 = Entry(master)
e8 = Entry(master)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)
e6.grid(row=6, column=1)
e7.grid(row=7, column=1)
e8.grid(row=8, column=1)

Button(master, text= "Okay",width= 100, command=display_text).grid(row=10,column=1)
mainloop()
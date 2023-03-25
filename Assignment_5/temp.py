from tkinter import *
import csv

window = Tk()
window.title("Blood bank donor form")
window.geometry('700x700')
window.configure(background = "white")
def thank():
    global age, tempill, permill, smoke, drugs, alcohol
    passed = Label(window, text = "Thanks for filling! We will contact you shortly.")
    failed = Label(window, text = "Sorry you are not eligible for donating blood.")
    u_age = age.get()
    print(u_age)
    # u_tempill = tempill.get()
    # u_permill = permill.get()
    # u_smoke = smoke.get()
    # u_drugs = drugs.get()
    # u_alcohol = alcohol.get()
    # if u_age >= 18 and u_tempill == "NIL" and u_permill == "NIL" and (u_smoke, u_drugs, u_alcohol) == ('N', 'N', 'N'):
    #     passed.grid(row = 15, column = 1)
    # else:
    #     failed.grid(row = 15, columns = 1)

Label(window ,text = "Name", bg = 'white').grid(row = 1,column = 0)
Label(window ,text = "Email Id", bg = 'white').grid(row = 2,column = 0)
Label(window ,text = "Age", bg = 'white').grid(row = 3,column = 0)
Label(window ,text = "Contact Number", bg = 'white').grid(row = 4,column = 0)
Label(window ,text = "Address", bg = 'white').grid(row = 5,column = 0)
Label(window ,text = "Blood Group", bg = 'white').grid(row = 6,column = 0)
Label(window ,text = "Have you had any illness in the past 6 months?\n NIL-No illness otherwise mention name of illness", bg = 'white').grid(row = 7,column = 0)
Label(window ,text = "Do you have any permanent illness?\n NIL-No illness otherwise mention name of illness", bg = 'white').grid(row = 8,column = 0)
Label(window ,text = "Do you drink alcohol?(Y/N)", bg = 'white').grid(row = 9,column = 0)
Label(window ,text = "Do you smoke?(Y/N)", bg = 'white').grid(row = 10,column = 0)
Label(window ,text = "Do you take drugs?(Y/N)", bg = 'white').grid(row = 11,column = 0)

fname = Entry(window).grid(row = 1,column = 1)
email = Entry(window).grid(row = 2,column = 1)
age = Entry(window)
age.grid(row = 3,column = 1)
number = Entry(window).grid(row = 4,column = 1)
address = Entry(window).grid(row = 5,column = 1)
bloodtype = Entry(window).grid(row = 6,column = 1)
tempill = Entry(window).grid(row = 7,column = 1)
permill = Entry(window).grid(row = 8,column = 1)
alcohol = Entry(window).grid(row = 9,column = 1)
smoke = Entry(window).grid(row = 10,column = 1)
drugs = Entry(window).grid(row = 11,column = 1)

Button(window ,text="Submit", command = thank).grid(row=14,column=0)

window.mainloop()
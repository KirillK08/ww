from tkinter import *

def plus():
    sk1 = (float(ent1.get()))
    sk2 = (float(ent2.get()))
    saskait = sk1 + sk2
    text.config(text = str(saskait))

def minus():
    sk1 = (float(ent1.get()))
    sk2 = (float(ent2.get()))
    atnemt = sk1 - sk2
    text.config(text = str(atnemt))

def reiz():
    sk1 = (float(ent1.get()))
    sk2 = (float(ent2.get()))
    reizināt = sk1 * sk2
    text.config(text = str(reizināt))

def dal():
    sk1 = (float(ent1.get()))
    sk2 = (float(ent2.get()))
    dalīt = sk1 / sk2
    text.config(text = str(dalīt))




wind = Tk()
wind.title("Aprēķini")
wind.geometry("400x300+500+200")

text = Label(wind, bg = "red", fg = "white", font = ("", 20), text = "Ievadiet divus skaitļus")
text.pack()

ent1 = Entry(wind, width = 25)
ent1.pack()

ent2 = Entry(wind, width = 25)
ent2.pack()

btn1 = Button(wind, bg = "blue", fg = "white", font = ("", 20), width = 25, text = "Saskaitīt", command = plus)
btn1.pack()

btn2 = Button(wind, bg = "blue", fg = "white", font = ("", 20), width = 25, text = "Atņemt", command = minus)
btn2.pack()

btn3 = Button(wind, bg = "blue", fg = "white", font = ("", 20), width = 25, text = "Reizināt", command = reiz)
btn3.pack()

btn4 = Button(wind, bg = "blue", fg = "white", font = ("", 20), width = 25, text = "Dalīt", command = dal)
btn4.pack()



wind.mainloop()
from tkinter import *
import calendar 

text=calendar.calendar(2022)
root=Tk()
root.geometry("500x600")
root.title("CALENDAR")

label=Label(root,text="CALENDAR",background="dark grey",font=("times new roman",28,"bold"))
label.grid(row=1,column=1)
label.config(background="white")

label2=Label(root,text=text,font="consolas 10 bold ")
label2.grid(row=2,column=1,padx=20)

root.mainloop()
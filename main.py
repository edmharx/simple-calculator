#create functions for addition, subtraction, multiplication, division
#create main loop
#import customtkinter
#design customtkinter
#connect buttons for function

import customtkinter as ctk
from tkinter import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

calc = ctk.CTk()
calc.geometry("360x500")
calc.title("Calculator")

i=0
func=""

def insert(value):
    global i
    global func
    current_num = entry.get()
    if current_num == 'Error':
        clear()
    else:
        current_num+=value
    if (value=="%"):
        value="/100"
    func+=value
    entry.insert(i, value)
    i += len(value)

def delete_last():
    global i
    global func
    current_num = entry.get()
    new_num = current_num[:-1]
    entry.delete(0, END)
    entry.insert(0, new_num)
    func = new_num
    i = len(new_num)

def clear():
    global func
    entry.delete(0,END)
    func = ""
    
def calculate():
    try:
        global func
        result=eval(func) #eval function to reduce lines and functions for simple calculations
        clear()
        entry.insert(0, result)
        func = str(result)
    except:
        entry.delete(0, END)
        entry.insert(0, 'Error')

#Entry Box
entry = ctk.CTkEntry(calc, placeholder_text="", width=320, height=60, font=('Arial',20))
entry.grid(padx=20, pady=10,)

#Buttons

button1 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="Del", command=delete_last, corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button1.place(x=20, y=80)

button2 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="C", command=clear, corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button2.place(x=100, y=80)

button3 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="+", command=lambda:insert("+"), corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button3.place(x=260, y=80)


button4 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="7", command=lambda:insert("7"), corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button4.place(x=20, y=160)

button5 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="8", command=lambda:insert("8"), corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button5.place(x=100, y=160)

button6 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="9", command=lambda:insert("9"), corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button6.place(x=180, y=160)

button7 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="-", command=lambda:insert("-"), corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button7.place(x=260, y=160)


button8 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="4", command=lambda:insert("4"), corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button8.place(x=20, y=240)

button9 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="5", command=lambda:insert("5"), corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button9.place(x=100, y=240)

button10 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="6", command=lambda:insert("6"), corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button10.place(x=180, y=240)

button11 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="/", command=lambda:insert("/"), corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button11.place(x=260, y=240)


button12 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="1", command=lambda:insert("1"), corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button12.place(x=20, y=320)

button13 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="2", command=lambda:insert("2"), corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button13.place(x=100, y=320)

button14 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="3", command=lambda:insert("3"), corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button14.place(x=180, y=320)

button15 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="x", command=lambda:insert("*"), corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button15.place(x=260, y=320)



button16 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="0", command=lambda:insert("0"), corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button16.place(x=100, y=400)

button17 = ctk.CTkButton(calc, height=80, width=160, hover=True, hover_color="black", text="=", command=calculate, corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button17.place(x=180, y=400)

button18 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="%", command=lambda:insert("%"), corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button18.place(x=180, y=80)

button19 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text=".", command=lambda:insert("."), corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button19.place(x=20, y=400)

calc.mainloop()
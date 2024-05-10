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


entry = ctk.CTkEntry(calc, placeholder_text="", width=320, height=60, font=('Arial',20))
entry.grid(padx=20, pady=10,)

#Buttons

button1 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="Del", command="button_event", corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button1.place(x=20, y=80)

button2 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="C", command="button_event", corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button2.place(x=100, y=80)

button3 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="+", command="button_event", corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button3.place(x=260, y=80)


button4 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="7", command="button_event", corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button4.place(x=20, y=160)

button5 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="8", command="button_event", corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button5.place(x=100, y=160)

button6 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="9", command="button_event", corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button6.place(x=180, y=160)

button7 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="-", command="button_event", corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button7.place(x=260, y=160)


button8 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="4", command="button_event", corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button8.place(x=20, y=240)

button9 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="5", command="button_event", corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button9.place(x=100, y=240)

button10 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="6", command="button_event", corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button10.place(x=180, y=240)

button11 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="/", command="button_event", corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button11.place(x=260, y=240)


button12 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="1", command="button_event", corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button12.place(x=20, y=320)

button13 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="2", command="button_event", corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button13.place(x=100, y=320)

button14 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="3", command="button_event", corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button14.place(x=180, y=320)

button15 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="X", command="button_event", corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button15.place(x=260, y=320)



button16 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="0", command="button_event", corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button16.place(x=100, y=400)

button17 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text=".", command="button_event", corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button17.place(x=180, y=400)

button18 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="=", command="button_event", corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button18.place(x=260, y=400)

button19 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="CE", command="button_event", corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button19.place(x=180, y=80)

button20 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="%", command="button_event", corner_radius=0, border_color="white", border_width=1, border_spacing=0, font=('Arial',20))
button20.place(x=20, y=400)

calc.mainloop()
#create functions for addition, subtraction, multiplication, division
#create main loop
#import customtkinter
#design customtkinter
#connect buttons for function

import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

calc = ctk.CTk()
calc.geometry("360x500")
calc.title("Calculator")


entry = ctk.CTkEntry(calc, placeholder_text="Enter number...", width=320, height=60)
entry.grid(padx=20, pady=10,)

#Buttons

button1 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="Del", command="button_event")
button1.place(x=20, y=80)

button2 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="C", command="button_event")
button2.place(x=100, y=80)

button3 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="+", command="button_event")
button3.place(x=260, y=80)


button4 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="7", command="button_event")
button4.place(x=20, y=160)

button5 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="8", command="button_event")
button5.place(x=100, y=160)

button6 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="9", command="button_event")
button6.place(x=180, y=160)

button7 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="-", command="button_event")
button7.place(x=260, y=160)


button8 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="4", command="button_event")
button8.place(x=20, y=240)

button9 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="5", command="button_event")
button9.place(x=100, y=240)

button10 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="6", command="button_event")
button10.place(x=180, y=240)

button11 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="/", command="button_event")
button11.place(x=260, y=240)


button12 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="1", command="button_event")
button12.place(x=20, y=320)

button13 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="2", command="button_event")
button13.place(x=100, y=320)

button14 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="3", command="button_event")
button14.place(x=180, y=320)

button15 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="X", command="button_event")
button15.place(x=260, y=320)



button16 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="0", command="button_event")
button16.place(x=100, y=400)

button17 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text=".", command="button_event")
button17.place(x=180, y=400)

button18 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="=", command="button_event")
button18.place(x=260, y=400)

button19 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="CE", command="button_event")
button19.place(x=180, y=80)

button20 = ctk.CTkButton(calc, height=80, width=80, hover=True, hover_color="black", text="%", command="button_event")
button20.place(x=20, y=400)

calc.mainloop()
from tkinter import *
from tkinter import messagebox
import customtkinter


def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)

##Ventana##
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")    
root = customtkinter.CTk()
root.geometry("800x400")
label = customtkinter.CTkLabel(master=root, text="texto :v", width= 120, height=25, fg_color=("black"), corner_radius=3)
label.place(relx=0.5, rely=0.5, anchor=CENTER)

button = customtkinter.CTkButton(master=root, width=120, height=25, border_width=0, corner_radius=3, text="boton", )
button.place(relx=0.5, rely=0.5, anchor=CENTER)


root.mainloop()
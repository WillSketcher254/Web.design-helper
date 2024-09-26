import os
import sys
import fileinput
import customtkinter
from tkinter import messagebox

def new_file():
    file = open("New.html","w+")
    file.write('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Document</title> </head><body></body></html>')
    messagebox.showinfo("INFO", "FIle created SUCCESFULLY !")

def add_style():
    textToSearch = '</title> '
    textToReplace = '</title><style>body{background: aqua;}</style> '
    tempfile = open("New.html", 'r+')
    for line in tempfile:
        tempfile.write(line.replace(textToSearch,textToReplace))
    tempfile.close()


app = customtkinter.CTk()
app.title('WEB_HELPER')
app.geometry('850x400')
app.resizable(False,False)
customtkinter.set_default_color_theme('dark-blue')

#Button1
create_html = customtkinter.CTkButton(app, text='Start_Creating', font=('Comic Sans MS', 18), hover_color='#8A2BE2', command=new_file)
create_html.place(x=50, y=50)

style_btn = customtkinter.CTkButton(app, text='Style', font=('Comic Sans MS', 18), hover_color='#8A2BE2', command=add_style)
style_btn.place(x=50, y=100)
app.mainloop()



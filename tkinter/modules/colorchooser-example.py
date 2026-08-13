# BASIC COLORCHOOSER MODULE EXAMPLE

import tkinter
from tkinter import ttk
import tkinter.colorchooser

win = tkinter.Tk()
win.title("Tkinter Color Chooser")

def changecolor():
    colors = tkinter.colorchooser.askcolor()
    win.configure(bg = colors[1])

ttk.Button(win, text = "Pick Color", command = changecolor).pack()
win.mainloop()
# This program creates a button saying 'Pick Color', on clicking which it asks to choose a color and then changes the background color to that color.

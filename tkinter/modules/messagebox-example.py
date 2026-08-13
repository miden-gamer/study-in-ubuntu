import tkinter as ttk
from tkinter import messagebox

def dialog():
    messagebox.showerror('answer', 'Sorry no ans available')

ttk.Button(text = 'Answer', command = dialog).pack()
ttk.mainloop()

"""
Tkinter
Tk
pip install tkinter
py2 Tkinter
py3 tkinter
4 Steps
1. Import tkinter module
2. window
3. add widgets
4. mainloop()
"""

# BASIC TKINTER WINDOW

import tkinter

win = tkinter.Tk()
# Arguments of Tk()
# 1. screenName: sets the display event
# 2. baseName: sets the base profile (by default it is derived from the program name)
# 3. className: it is name of widget that is currently used widget class (it is Tk here)
# 4. useTk: if it is True it initializes Tk subsystem
# 5. sync: it is used for debugging, basically it executes all xserver commands synchronously
# 6. use: specifies ID of the window for application

# Set the title of the window
win.title("First Tkinter Window")

win.mainloop()
# The logo (if shown) by default is the logo of Tk, and even title by default is tk.

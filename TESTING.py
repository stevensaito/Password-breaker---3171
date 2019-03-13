from tkinter import *
from subprocess import call
import os   #import for command promt
from tkinter import *
fields = 'Command'     #Makes the field

def callpy(): os.system("start cmd")



root = Tk()

#BUTTONS
Button(root, text='Quit', command=root.quit).pack(side=LEFT, padx=5, pady=5)
Button(root, text='Run', command=callpy).pack(side=RIGHT, padx=5, pady=5)

root.mainloop()
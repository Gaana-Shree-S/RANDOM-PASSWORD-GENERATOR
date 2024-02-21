import tkinter
from tkinter import messagebox
import random
import string


def calculate():
    characterList = ""
    n=8
    while(n>=0):
        choice = random.ranint(1,3)
        if(choice == 1):
            characterList += string.ascii_letters
        if(choice == 2):
            characterList += string.digits
        if(choice == 3):
            characterList += string.punctuation
        n=n-1
    messagebox.showinfo("PASSWORD", characterList)

            
    
#Creating a display window
window=tkinter.Tk()
window.geometry('400x400')
label=tkinter.Label(window, text="RANDOM PASSWORD GENERATOR")
label.pack()
var =tkinter.IntVar()

frame=tkinter.Frame(window, padx=5, pady=5)
frame.pack(expand=True)
noc=tkinter.Label(frame, text="ENTER THE NUMBER OF CHARACTERS")
noc.grid(row=1,column=2)
n=tkinter.Entry(frame,)
n.grid(row=2,column=2)

c=tkinter.Button(frame,text="Confirm",command=calculate)
c.grid(row=3, column=2)
#Window will be displayed as long as user terminates
window.mainloop()

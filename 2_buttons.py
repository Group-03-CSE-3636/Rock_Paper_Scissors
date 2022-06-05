from tkinter import *
window = Tk()

def myClick():
    myLabel= Label(window, text="Look! I clicked a button!!")
    myLabel.pack()

window.title("GUI")

myButton=Button(window, text="Click!", padx=25, pady=20, command= myClick, fg="#0C4081", bg="#6AE5FF")
myButton.pack()

window.mainloop()
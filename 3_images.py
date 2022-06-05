from tkinter import *
from PIL import ImageTk,Image
window = Tk()
window.title("GUI")
window.iconbitmap('g:/RockPaperScissors/star.ico')

img=ImageTk.PhotoImage(Image.open("pet.jpg"))
label=Label(image=img)
label.pack()



button_quit=Button(window, text="Exit Program", command=window.quit)
button_quit.pack()

window.mainloop()
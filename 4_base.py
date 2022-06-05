from distutils import command
from tkinter import *
from PIL import ImageTk , Image
window = Tk()
window.title('My First Window')
# window.iconbitmap('g:/pyt/star.ico')

def open():
 global img
 top=Toplevel()
 top.title('My Second Window')
 top.iconbitmap('g:/pyt/star.ico')
 img=ImageTk.PhotoImage(Image.open("pet.jpg"))
 label=Label(top, image=img).pack()
 button2=Button(top, text="Close Window", command=top.destroy).pack()

button1=Button(window, text="Open Second Window", command=open).pack()

mainloop()
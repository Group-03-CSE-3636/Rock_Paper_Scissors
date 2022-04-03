from tkinter import *
from PIL import Image, ImageTk
from random import randint


#main window

root = Tk()
root.title("Rock Paper Scissor")
root.iconbitmap('g:/RockPaperScissors/star.ico')
root.configure(background="#B16B9E")


# root.geometry("960x540")

# bg=PhotoImage(file="images/b5.png")

# my_label=Label(root, image=bg)



#pictures
rock_img= ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img= ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img= ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp= ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp= ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp= ImageTk.PhotoImage(Image.open("scissors.png"))

#insert pictures
user_label= Label(root,image=scissor_img, bg="#B16B9E")
comp_label= Label(root,image=scissor_img_comp, bg="#B16B9E")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

#scores
playerScore = Label(root,text=0,font=100,bg="#B16B9E",fg="white")
computerScore = Label(root,text=0,font=100,bg="#B16B9E",fg="white")
computerScore.grid(row=1, column=1)
computerScore.grid(row=1, column=3)

#buttons


root.mainloop()
from tkinter import *
from PIL import Image, ImageTk
from random import randint

#main window
root = Tk()
root.geometry('1015x500')
root.resizable(0,0)
root.title("Rock Paper Scissor")
root.iconbitmap('g:/RockPaperScissors/images/game_icon.ico')
root.configure(background="#9b59b6")


gametitle = Label(root, text='Rock, Paper ,Scissors', font='arial 20 bold', bg="#9b59b6", fg="antiquewhite2")
gametitle.grid(row=0, column=2)


# picture
rock_img = ImageTk.PhotoImage(Image.open("images/rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("images/paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("images/scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("images/rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("images/paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("images/scissors.png"))

# insert picture
user_label = Label(root, image=scissor_img, bg="#9b59b6")
comp_label = Label(root, image=scissor_img_comp, bg="#9b59b6")
comp_label.grid(row=2, column=0)
user_label.grid(row=2, column=4)


# scores
playerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore.grid(row=2, column=1)
playerScore.grid(row=2, column=3)

# indicators
user_indicator = Label(root, font=50, text="PLAYER", bg="#9b59b6", fg="white")
comp_indicator = Label(root, font=50, text="COMPUTER",bg="#9b59b6", fg="white")
user_indicator.grid(row=1, column=3)
comp_indicator.grid(row=1, column=1)

# messages
msg = Label(root, font='arial 20 bold', bg="#9b59b6", fg="white")
msg.grid(row=7, column=2)


def closeWin():
 root.destroy()

# Reset The Game
def reset_game():
    playerScore.config(text =0)
    computerScore.config(text =0)


# update message
def updateMessage(x):
    msg['text'] = x


# update user score
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)


# update computer score
def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)


# check winner
def checkWin(player, computer):
    if player == computer:
        updateMessage("Its a tie!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()

    else:
        pass


# update choices
choices = ["rock", "paper", "scissor"]


def updateChoice(x):

    # for computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)


# for user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x, compChoice)


Chossebutton = Label(root, text='choose any one: rock, paper, scissors', font='arial 13 bold',fg = "#D6FF60", bg="#9b59b6",)
Chossebutton.grid(row=3, column=2)

space1 = Label(root, bg="#9b59b6")
space1.grid(row=4, column=2)



# buttons
rock = Button(root, width=20, height=2, text="ROCK",
              bg="#FF3E4D", fg="white", command=lambda: updateChoice("rock")).grid(row=5, column=1)
paper = Button(root, width=20, height=2, text="PAPER",
               bg="#FAD02E", fg="white", command=lambda: updateChoice("paper")).grid(row=5, column=2)
scissor = Button(root, width=20, height=2, text="SCISSORS",
                 bg="#0ABDE3", fg="white", command=lambda: updateChoice("scissor")).grid(row=5, column=3)
quit = Button(root, font='arial 13 bold',text="Quit Game",fg = "yellow",
              bg ='black', command = closeWin).grid(row=8, column=4)
reset = Button(root, font='arial 13 bold',text="Reset Game",fg = "red", 
               bg = "black", command = reset_game).grid(row=8, column=0)

space2 = Label(root, bg="#9b59b6")
space2.grid(row=6, column=2)



root.mainloop()

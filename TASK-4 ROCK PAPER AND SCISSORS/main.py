from tkinter import*
import random

# FUNCTIONS

def rockplay():
    playing_game("Rock")

def paperplay():
    playing_game("Paper")

def scissorplay():
    playing_game("Scissors")

# INITIALISING SCORES

user_score = 0
computer_score = 0
game_history = []

# DETERMINING WINNER + UPDATING

def playing_game(user_choice):
    global user_score, computer_score, game_history
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        result = "It's a Tie !"
    elif ((user_choice == 'Rock' and computer_choice == 'Scissors') or
          (user_choice == 'Paper' and computer_choice == 'Rock') or
          (user_choice == 'Scissors' and computer_choice == 'Paper')):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    # UPDATING LABELS

    userlb.config(text=f"Your Choice : {user_choice}")
    complb.config(text=f"Computer's Choice : {computer_choice}")
    resultlb.config(text=f"Result : {result}")
    scorelb.config(text=f"Your Score: {user_score}    Computer's Score: {computer_score}")

    # UPDATE THE GAME HISTORY
    game_history.append(f"YOU: {user_choice} | COMPUTER: {computer_choice} | RESULT: {result}")
    update_his()

def update_his():
    game_listbox.delete(0,END)
    for match in game_history:
        game_listbox.insert(END, match)

def replay():
    global user_score, computer_score, game_history
    user_score = 0
    computer_score = 0
    game_history = []
    update_his()
    userlb.config(text=f"Your Choice : ")
    complb.config(text=f"Computer's Choice : ")
    resultlb.config(text=f"Result : ")
    scorelb.config(text="Your Score: 0    Computer's Score: 0")

# MAIN WINDOW

root = Tk()
root.title("Rock - Paper - Scissors Game")
root.geometry("600x340")
root.wm_iconbitmap("rps.ico")

#HEADING

Label(root, text="ROCK PAPER SCISSORS GAME", font="comicsansms 18 bold", pady=15).grid(row=0, column=1, columnspan=4, padx=40)

# REQUIRED LABELS

userlb = Label(root, text="Your Choice : ")
complb = Label(root, text="Computer's Choice : ")
resultlb = Label(root, text="Result :")
scorelb = Label(root, text="Your Score: 0    Computer's Score: 0")

#PACKING THE LABELS
#columnspan = To fix the columns widget will occupy

userlb.grid(row=1, column=1, columnspan=2)      
complb.grid(row=2, column=1, columnspan=2)
resultlb.grid(row=3, column=1, columnspan=2, padx=5)
scorelb.grid(row=4, column=1, columnspan=2, padx=5)

# CREATING BUTTONS

rockbt = Button(root, text="ROCK", command=rockplay)
paperbt = Button(root, text="PAPER", command=paperplay)
scissorbt = Button(root, text="SCISSORS", command=scissorplay)
replaybt = Button(root, text="RE-PLAY", command=replay)

# PACKING BUTTONS

rockbt.grid(row=1, column=0, padx=5, pady=5)
paperbt.grid(row=2, column=0, padx=5, pady=5)
scissorbt.grid(row=3, column=0, padx=5, pady=5)
replaybt.grid(row=4, column=0, padx=5, pady=5)

# LISTBOX

game_listbox = Listbox(root, width=50, height=15)
game_listbox.grid(row=1,rowspan=4, column=3, columnspan=4)

# ADDING SCROLL BAR AS RULES SAY

Scroll = Scrollbar(root, orient=VERTICAL)
game_listbox.config(yscrollcommand=Scroll.set)
Scroll.grid(row=1,rowspan=4, column=7, columnspan=7, sticky="ns")
Scroll.config(command= game_listbox.yview)

# RUN THE APPLICATION
root.mainloop()
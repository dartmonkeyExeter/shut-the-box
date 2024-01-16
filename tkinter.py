import tkinter as tk
from random import randint
from time import sleep
from itertools import combinations

master = tk.Tk()
master.geometry(f"440x125")
master.resizable(False, False)
master.title("TKINER!!!! TESTING!!!")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
box = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number_buttons = []
user_choices = []
total = 0
current_player = 0
player_amount = 0
player_points = []

def Reset():
    global box
    global user_choices
    global total

    box = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    user_choices = []
    total = 0
    display_roll.config(text=total)

    for i in numbers:
        number_buttons[i - 1].config(state="normal")
        number_buttons[i - 1].config(bg="dark sea green")
    
    roll_one.config(state="disabled")
    roll_two.config(state="normal")

def Roll_Dice(amount):
    global total
    roll_one.config(state="disabled")
    roll_two.config(state="disabled")
    total = 0
    for i in range(amount):
        total += randint(1, 6)
    display_roll.config(text=total)

    possible_rolls = Get_Possible_Rolls()

    if len(possible_rolls) == 0:
        Reset()

    return total

def Get_Possible_Rolls():
    global box
    global total
    possible_combinations = []
    for r in range(1, len(box) + 1):
        possible_combinations.extend(combinations(box, r))
    possible_rolls = []
    for combination in possible_combinations:
        if sum(combination) == total:
            possible_rolls.append(combination)
            break
    return possible_rolls

def Eliminate_Numbers(box, user_choices):
    return [x for x in box if x not in user_choices]

def Confirm(number_buttons):
    global box
    global numbers
    global user_choices
    global total

    user_choices = list(user_choices)
    user_choices.sort()
    user_choices = tuple(user_choices)
    if user_choices in combinations(box, len(user_choices)) and sum(user_choices) == total:
        box = Eliminate_Numbers(box, user_choices)
        user_choices = []
        total = 0
        display_roll.config(text=total)
        roll_two.config(state="normal")
        if 7 not in box and 8 not in box and 9 not in box:
            roll_one.config(state="normal")
    else:
        for i in numbers:
            if i in box:
                number_buttons[i - 1].config(bg="dark sea green")
    for i in numbers:
        if i not in box:
            number_buttons[i - 1].config(state="disabled")
            number_buttons[i - 1].config(bg="red")

def User_Choice(i):
    global user_choices
    global number_buttons

    user_choices = list(user_choices)
    if i + 1 in user_choices:
        user_choices.remove(i + 1)
        number_buttons[i].config(bg="dark sea green")
    else:
        user_choices.append(i + 1)
        number_buttons[i].config(bg="light pink")


for i in range(9):
    cur = tk.Button(text=f"{i + 1}", width=2, height=1, font=("Comic Sans MS", 12, "bold"), 
                                    command=lambda i=i: User_Choice(i))
    cur.config(bg="dark sea green")
    number_buttons.append(cur)

confirm = tk.Button(text="Confirm", width=10, height=1, font=("Comic Sans MS", 12, "bold"), command=lambda: Confirm(number_buttons))
confirm.config(bg="medium sea green")

display_roll = tk.Label(text=total, width=10, height=1, font=("Comic Sans MS", 12, "bold"))
roll_one = tk.Button(text="1 DICE", width=5, height=1, font=("Comic Sans MS", 6, "bold"), command=lambda: Roll_Dice(1))
roll_two = tk.Button(text="2 DICE", width=5, height=1, font=("Comic Sans MS", 6, "bold"), command=lambda: Roll_Dice(2))

for idx, button in enumerate(number_buttons):
    button.place(x=55 + ((idx - 1) * 50), y=20)

confirm.place(x=165, y=65)

display_roll.place(x=55, y=70)
roll_one.place(x=5, y=65)
roll_two.place(x=5, y=90)

roll_one.config(state="disabled")
roll_two.config(state="normal")

master.mainloop()

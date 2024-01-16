import tkinter as tk
from random import randint
from itertools import combinations

master = tk.Tk()
master.geometry(f"440x100")
master.resizable(False, False)
master.title("TKINER!!!! TESTING!!!")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
box = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number_buttons = []
user_choices = []
total = 0

def Roll_Dice():
    global total
    total = randint(1, 6) + randint(1, 6)
    display_roll.config(text=total)
    return total

def Get_Possible_Rolls(box, total):
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

def Confirm(number_buttons, total, user_choices):
    global box

    user_choices.sort()
    user_choices = tuple(user_choices)
    if user_choices in combinations(box, len(user_choices)) and sum(user_choices) == total:
        box = Eliminate_Numbers(box, user_choices)
    else:
        print(user_choices, box, total, sum(user_choices))
    
    for i in numbers:
        if i not in box:
            number_buttons[i - 1].config(state="disabled")
            number_buttons[i - 1].config(bg="red")

    user_choices = []

    Roll_Dice()

def User_Choice(i):
    global user_choices
    user_choices = list(user_choices)
    if i + 1 in user_choices:
        user_choices.remove(i + 1)
        number_buttons[i].config(bg="dark sea green")
    else:
        user_choices.append(i + 1)
        number_buttons[i].config(bg="light pink")
    


for i in range(9):
    cur = tk.Button(text=f"{i + 1}", width=2, height=1, font=("Arial", 12, "bold"), 
                                    command=lambda i=i: User_Choice(i))
    cur.config(bg="dark sea green")
    number_buttons.append(cur)

confirm = tk.Button(text="Confirm", width=10, height=1, font=("Arial", 12, "bold"), command=lambda: Confirm(number_buttons, total, user_choices))
confirm.config(bg="medium sea green")

display_roll = tk.Label(text=total, width=10, height=1, font=("Arial", 12, "bold"))
total = Roll_Dice()

for idx, button in enumerate(number_buttons):
    button.place(x=55 + ((idx - 1) * 50), y=10)

confirm.place(x=165, y=55)
display_roll.place(x=55, y=55)

master.mainloop()
print(box)

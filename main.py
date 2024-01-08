# shut the box
from random import randint
from itertools import combinations

def get_number_of_players():
    while True:
        try:
            how_many_players = int(input("How many players? "))
            return how_many_players
        except ValueError:
            print("Invalid input")

def get_player_names(num_players):
    players = []
    for i in range(num_players):
        players.append(input("Name of player " + str(i + 1) + ": "))
    return players

def roll_dice():
    return randint(1, 6) + randint(1, 6)

def get_possible_rolls(box, total):
    possible_combinations = []
    for r in range(1, len(box) + 1):
        possible_combinations.extend(combinations(box, r))
    possible_rolls = []
    for combination in possible_combinations:
        if sum(combination) == total:
            possible_rolls.append(combination)
            break
    return possible_rolls

def eliminate_numbers(box, to_eliminate):
    return [x for x in box if x not in to_eliminate]

def play_game():
    
    players = get_player_names(get_number_of_players())
    points = []

    for player in players:
        print("It's " + player + "'s turn!")
        box = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        total = 0
        while True:
            total = roll_dice()

            if 7 not in box and 8 not in box and 9 not in box:
                roll_two_dice = input("Roll 1 or 2 dice? ")
                if roll_two_dice == "2":
                    total = roll_dice()
                elif roll_two_dice == "1":
                    total = randint(1, 6)
                else:
                    print("Invalid input")
                    continue
            possible_rolls = get_possible_rolls(box, total)
            
            print("Numbers left: ", box)
            print("Roll: ", total)

            if len(possible_rolls) == 0:
                print("no possible moves")
                points.append(sum(box))
                break

            while True:
                try:
                    to_eliminate = input("Numbers to eliminate (as comma separated list): ")
                    to_eliminate = to_eliminate.split(",")
                    to_eliminate = [int(i) for i in to_eliminate]
                    to_eliminate.sort()
                    to_eliminate = tuple(to_eliminate)
                except ValueError:
                    print("Invalid input")
                    continue
                if to_eliminate in combinations(box, len(to_eliminate)) and sum(to_eliminate) == total:
                    box = eliminate_numbers(box, to_eliminate)                
                    break 

    for idx, player in enumerate(players):
        print(player + ": " + str(points[idx]))
play_game()


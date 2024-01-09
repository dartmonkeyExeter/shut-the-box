# shut the box
from random import randint
from itertools import combinations

# Function to get the number of players
def get_number_of_players():
    while True:
        try:
            how_many_players = int(input("How many players? "))
            return how_many_players
        except ValueError:
            print("Invalid input")

# Function to get the names of the players
def get_player_names(num_players):
    players = []
    for i in range(num_players):
        players.append(input("Name of player " + str(i + 1) + ": "))
    return players

# Function to roll the dice
def roll_dice():
    return randint(1, 6) + randint(1, 6)

# Function to get possible rolls based on the current state of the box
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

# Function to eliminate numbers from the box
def eliminate_numbers(box, to_eliminate):
    return [x for x in box if x not in to_eliminate]

# Function to play the game
def play_game():
    players = get_player_names(get_number_of_players())  # Get player names
    points = [0 for i in range(len(players))]  # Initialize points for each player

    while players:
        for player in players:
            print("It's " + player + "'s turn!")
            box = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Initialize the box with numbers 1 to 9
            total = 0

            while True:
                total = roll_dice()  # Roll the dice

                # Check if only 7, 8, and 9 are left in the box
                if 7 not in box and 8 not in box and 9 not in box:
                    roll_two_dice = input("Roll 1 or 2 dice? ")
                    if roll_two_dice == "2":
                        total = roll_dice()  # Roll two dice
                    elif roll_two_dice == "1":
                        total = randint(1, 6)  # Roll one die
                    else:
                        print("Invalid input")
                        continue

                possible_rolls = get_possible_rolls(box, total)  # Get possible rolls based on the current state of the box

                print("Numbers left: ", box)
                print("Roll: ", total)

                if len(possible_rolls) == 0:
                    print("No possible moves")
                    points[players.index(player)] += sum(box)  # Add the sum of remaining numbers to the player's points
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
                        box = eliminate_numbers(box, to_eliminate)  # Eliminate numbers from the box
                        break

        for idx, player in enumerate(players):
            print(player + ": " + str(points[idx]))  # Print the points of each player

        for i in range(len(players)):
            if points[i - 1] >= 45:
                print(players[i - 1] + " lost!")
                players.pop(i - 1)  # Remove the player who lost from the list of players
                points.pop(i - 1)  # Remove the points of the player who lost
                break

        if len(players) == 1:
            print(players[0] + " won!")
            break

play_game()  # Start the game

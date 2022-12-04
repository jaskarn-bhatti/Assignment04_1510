"""
Jaskarn
Student number: A01328100
"""

from art import the_big_top
from art import clown
from art import monkey
import math


def make_board(rows, columns):
    a = {}
    for length in range(columns):
        for width in range(rows):
            if length == 1 and width == 1 or length == 4 and width == 2:
                a[length, width] = "Quest"
            elif length == 0 and width == 4:
                a[length, width] = "Boss"
            else:
                a[length, width] = "Empty room"
    return a


def make_character(user_name):
    user_stats = {"Name": user_name, "X-coordinate": 0, "Y-coordinate": 0, "Current HP": 10, "Attack Damage": 5,
                  "level": 1}
    return user_stats


def describe_current_location(board, character):
    character_pos = (character.get("X-coordinate"), character.get("Y-coordinate"))
    board_key = list(board.keys())
    current_board = []
    for size in range(len(board_key)):
        if character_pos == board_key[size]:
            current_board.append('0')
        elif board.get(board_key[size]) == "Quest":
            current_board.append('Q')
        elif board.get(board_key[size]) == "Boss":
            current_board.append('F')
        else:
            current_board.append('X')

    i = 0
    while i < 5:
        print(current_board[0:5])
        del current_board[0:5]
        i += 1


def get_user_choice():
    print("\nMovement Key")
    print("West: w  North: n  East: e  South: s")
    movement_number = str(input("Enter direction: "))
    movement_number = movement_number.lower()
    if movement_number == 'w' or movement_number == 'n' or movement_number == 'e' or movement_number == 's':
        return movement_number
    else:
        print("Enter movement direction again")
        get_user_choice()


def validate_move(character, direction):
    if direction == "n":
        if character["X-coordinate"] - 1 < 0:
            return False
    elif direction == "s":
        if character["X-coordinate"] + 1 > 4:
            return False
    elif direction == "w":
        if character["Y-coordinate"] - 1 < 0:
            return False
    elif direction == "e":
        if character["Y-coordinate"] + 1 > 4:
            return False
    return True


def move_character(character, direction):
    if direction == "n":
        character["X-coordinate"] = character["X-coordinate"] - 1
    elif direction == "s":
        character["X-coordinate"] = character["X-coordinate"] + 1
    elif direction == "w":
        character["Y-coordinate"] = character["Y-coordinate"] - 1
    else:
        character["Y-coordinate"] = character["Y-coordinate"] + 1


def check_for_quest(character, board):
    if board[character["X-coordinate"], character["Y-coordinate"]] == "Quest":
        return True
    else:
        return False


def execute_challenge_protocol(character):
    print("\nBattle")
    print("Fight the clown to death")
    clown()
    clown_stats = {"Current HP": 10, "Attack Damage": 2}

    clown_dead = False
    while not clown_dead:
        if clown_stats["Current HP"] <= 0:
            print("\nClown has been killed.")
            character["level"] += 1
            print("You have leveled up to level", character["level"])
            character["Current HP"] += 5
            character["Attack Damage"] += 1
            print("Player stats\nHP:", character["Current HP"], "\nAttack Damage:", character["Attack Damage"], "\n")
            clown_dead = True
        else:
            print("\nMoves\npunch: 1 kick: 2 run: 3 ")
            move = int(input("Enter move: "))

            if move == 1:
                clown_stats["Current HP"] = clown_stats["Current HP"] - character["Attack Damage"]
                character["Current HP"] = character["Current HP"] - clown_stats["Attack Damage"]
                print("\nThe clown did 2 damage.")
                print("Your HP:", character["Current HP"])
                print("You did", character["Attack Damage"] ,"damage")
                print("Clown HP:", clown_stats["Current HP"])
            elif move == 2:
                clown_stats["Current HP"] = clown_stats["Current HP"] - math.floor(character["Attack Damage"] * 0.8)
                character["Current HP"] = character["Current HP"] - clown_stats["Attack Damage"]
                print("\nThe clown did 2 damage.")
                print("Your HP:", character["Current HP"])
                print("You did", math.floor(character["Attack Damage"] * 0.8), "damage")
                print("Clown HP:", clown_stats["Current HP"])
            elif move == 3:
                print("\nYou can not run from a clown.")
                print("You got clowned for trying to run -2 HP.")
                character["Current HP"] = character["Current HP"] - clown_stats["Attack Damage"]
                print("Your HP:", character["Current HP"])
                print("Clown HP:", clown_stats["Current HP"])
            else:
                print("\nWrong number!!!")
                character["Current HP"] = character["Current HP"] - clown_stats["Attack Damage"]
                print("You lost -2 HP for wrong number.")
                print("Your HP:", character["Current HP"])
                print("Clown HP:", clown_stats["Current HP"])

def final_boss(character):
    print("\nBattle")
    print("Fight the clown to death")
    mokey()
    clown_stats = {"Current HP": 10, "Attack Damage": 2}



def game():  # called from main
    print("Gravestone Circus")
    the_big_top()
    print("April 13, 1990 you go out to watch magical monkey preform.")
    print("You arrive at the Circus to find yourself the only one in attendance.")
    print("As the show begins you see a big flash.")
    print("Your eyes open to realize that the exit is guarded by a giant monkey.\n")
    print("Escape the Gravestone Circus !!!")
    print("Hello adventure")
    user_name = input("Enter your name: ")
    print("\nGame Rules:")
    print("Go around the map to fight the quest.")
    print("If you are feeling lucky challenge the finial boss!")
    print("Map details:")
    print("0 = players current position")
    print("X = spots on map")
    print("Q = Quest")
    print("F = Finial Boss\n")

    # makes board dictionary
    rows = 5
    columns = 5
    board = make_board(rows, columns)

    # Make character profile
    character = make_character(user_name)

    achieved_goal = False
    while not achieved_goal:
        # Tell the user where they are
        describe_current_location(board, character)

        direction = get_user_choice()
        valid_move = validate_move(character, direction)

        if valid_move:
            move_character(character, direction)
            there_is_a_challenge = check_for_quest(character, board)
            if there_is_a_challenge:
                execute_challenge_protocol(character)
            elif board[character["X-coordinate"], character["Y-coordinate"]] == "Boss":
                final_boss(character)
    # achieved_goal = check_if_goal_attained(board, character)
    # else:
    # # Print end of game stuff like congratulations or sorry you died
    #


def main():
    game()


if __name__ == "__main__":
    main()

"""
Jaskarn
Student number: A01328100
"""

from art import the_big_top
from art import clown
from art import monkey
from art import firework
from art import death
import math
import itertools


def make_board(rows, columns):
    """
    This make_board takes in rows and columns parameter to determine how big the board should be.

    It uses two for loops to populate every position with a coordinate value and a room type.

    :param rows: positive int value
    :param columns: positive int value
    :precondition: must be a positive int values greater than 0
    :postcondition: populates each square on board with coordinate and room type
    :return: the board dictionary which contains room coordinate and room type

    >>> make_board(5,7)
    {(0, 0): 'Empty room', (0, 1): 'Empty room', (0, 2): 'Empty room', (0, 3): 'Empty room', (0, 4): 'Boss', (1, 0): 'Empty room', (1, 1): 'Quest', (1, 2): 'Empty room', (1, 3): 'Empty room', (1, 4): 'Empty room', (2, 0): 'Empty room', (2, 1): 'Empty room', (2, 2): 'Empty room', (2, 3): 'Empty room', (2, 4): 'Empty room', (3, 0): 'Empty room', (3, 1): 'Empty room', (3, 2): 'Empty room', (3, 3): 'Empty room', (3, 4): 'Empty room', (4, 0): 'Empty room', (4, 1): 'Empty room', (4, 2): 'Quest', (4, 3): 'Empty room', (4, 4): 'Empty room', (5, 0): 'Empty room', (5, 1): 'Empty room', (5, 2): 'Empty room', (5, 3): 'Empty room', (5, 4): 'Empty room', (6, 0): 'Empty room', (6, 1): 'Empty room', (6, 2): 'Empty room', (6, 3): 'Empty room', (6, 4): 'Empty room'}

    >>> make_board(1,1)
    {(0, 0): 'Empty room'}

    >>> make_board(0,0)
    {}

    """
    board = {}
    for length in range(columns):
        for width in range(rows):
            if length == 1 and width == 1 or length == 4 and width == 2:
                board[length, width] = "Quest"
            elif length == 0 and width == 4:
                board[length, width] = "Boss"
            else:
                board[length, width] = "Empty room"
    return board


def make_character(user_name):
    """
    Make_character accepts the user_name from an input and then creates a dictionary with user info which contains
    username.

    :param user_name: string
    :precondition: user enters a string
    :postcondition: creates user dictionary and adds a user_name from the input
    :return: dictionary with user_stats

    >>> make_character("a")
    {'Name': 'a', 'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 10, 'Attack Damage': 5, 'level': 0}

    >>> make_character("chris")
    {'Name': 'chris', 'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 10, 'Attack Damage': 5, 'level': 0}

    >>> make_character("Celestial Dragon")
    {'Name': 'Celestial Dragon', 'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 10, 'Attack Damage': 5, 'level': 0}

    >>> make_character("123")
    {'Name': '123', 'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 10, 'Attack Damage': 5, 'level': 0}

    >>> make_character("$")
    {'Name': '$', 'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 10, 'Attack Damage': 5, 'level': 0}

    """
    user_stats = {"Name": user_name, "X-coordinate": 0, "Y-coordinate": 0, "Current HP": 10, "Attack Damage": 5,
                  "level": 0}
    return user_stats


def describe_current_location(board, character):
    """
    Takes board and character parameter and crates a dictionary which contains characters which represent the board.

    The dictionary is taken into a while loop and prints out each row.

    :param board: a dictionary with coordinates and room type
    :param character: a dictionary with x and y coordinates
    :precondition: board dictionary containing room types and character dictionary with x y coordinates
    :postcondition: prints each row of board with values


    """
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

    int_iterator = 0
    while int_iterator < 5:
        print(current_board[0:5])
        del current_board[0:5]
        int_iterator += 1


def get_user_choice():
    """
    Ask user to enter a direction to move and can type quit to quit the game.

    :precondition: user must enter w,n,s,e to move or quit to quit
    :postcondition: determines what direction the user wants to move or quit
    :return: direction the user wants to move or quit

    """
    print("\nMovement Key")
    print("West: w  North: n  East: e  South: s")
    movement_number = str(input("Enter direction: "))
    movement_number = movement_number.lower()
    if movement_number == 'w' or movement_number == 'n' or movement_number == 'e' or movement_number == 's':
        return movement_number
    elif movement_number == "quit":
        return "quit"
    else:
        print("Enter movement direction again")
        get_user_choice()


def validate_move(character, direction):
    """
    Checks if the user is able to move in that direction.

    :param character: a dictionary with x and y coordinates
    :param direction: a char either n,s,w,e
    :precondition: the dictionaries must contain correct values
    :postcondition: if move is feasible return true
    :return: true or false depending on if move is feasible

    >>> character = {'Name': '$', 'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 10, 'Attack Damage': 5, 'level': 0}
    >>> direction = "e"
    >>> validate_move(character, direction)
    True

    >>> character = {'Name': '$', 'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 10, 'Attack Damage': 5, 'level': 0}
    >>> direction = "w"
    >>> validate_move(character, direction)
    False

    >>> character = {'Name': '$', 'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 10, 'Attack Damage': 5, 'level': 0}
    >>> direction = "n"
    >>> validate_move(character, direction)
    False

    >>> character = {'Name': '$', 'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 10, 'Attack Damage': 5, 'level': 0}
    >>> direction = "s"
    >>> validate_move(character, direction)
    True

    >>> character = {'Name': '$', 'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 10, 'Attack Damage': 5, 'level': 0}
    >>> direction = "n"
    >>> validate_move(character, direction)
    True

     >>> character = {'Name': '$', 'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 10, 'Attack Damage': 5, 'level': 0}
    >>> direction = "w"
    >>> validate_move(character, direction)
    True

    """
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
    """
    Moves the player x and y depending on the direction.

    :param character: a dictionary with x and y coordinates
    :param direction: a char either n,s,w,e

    """
    if direction == "n":
        character["X-coordinate"] = character["X-coordinate"] - 1
    elif direction == "s":
        character["X-coordinate"] = character["X-coordinate"] + 1
    elif direction == "w":
        character["Y-coordinate"] = character["Y-coordinate"] - 1
    else:
        character["Y-coordinate"] = character["Y-coordinate"] + 1


def check_for_quest(character, board):
    """
    Checks if user is on the quest coordinates.

    :param character: a dictionary with x and y coordinates
    :param board: a dictionary with coordinates and room type
    :return: True or False if on quest


    """
    if board[character["X-coordinate"], character["Y-coordinate"]] == "Quest":
        return True
    else:
        return False


def execute_challenge_protocol(character):
    """
    Calls the clown to fight

    :param character: a dictionary with x and y coordinates
    :return: true or false if you beat the clowm
    """
    print("\nBattle")
    print("Fight the clown to death")
    clown()
    clown_stats = {"Current HP": 10, "Attack Damage": 2}

    clown_dead = False
    while not clown_dead:
        if clown_stats["Current HP"] <= 0:
            print("\nClown has been killed.")
            character["level"] += 1
            print("You have leveled up to level %s" % character["level"])
            character["Current HP"] += 5
            character["Attack Damage"] += 1
            print("Player stats\nHP: %s \nAttack Damage: %s\n" % (character["Current HP"], character["Attack Damage"]))
            clown_dead = True
        elif character["Current HP"] <= 0:
            return True
        else:
            print("\nMoves\npunch: 1 kick: 2 run: 3 ")
            move = int(input("Enter move: "))

            if move == 1:
                clown_stats["Current HP"] = clown_stats["Current HP"] - character["Attack Damage"]
                character["Current HP"] = character["Current HP"] - clown_stats["Attack Damage"]
                print("\nThe clown did 2 damage.")
                print("Your HP: %s" % character["Current HP"])
                print("You did %s damage" % character["Attack Damage"])
                print("Clown HP: %s" % clown_stats["Current HP"])
            elif move == 2:
                clown_stats["Current HP"] = clown_stats["Current HP"] - math.floor(character["Attack Damage"] * 0.8)
                character["Current HP"] = character["Current HP"] - clown_stats["Attack Damage"]
                print("\nThe clown did 2 damage.")
                print("Your HP: %s" % character["Current HP"])
                print("You did %s damage" % math.floor(character["Attack Damage"] * 0.8))
                print("Clown HP: %s" % clown_stats["Current HP"])
            elif move == 3:
                print("\nYou can not run from a clown.")
                print("You got clowned for trying to run -2 HP.")
                character["Current HP"] = character["Current HP"] - clown_stats["Attack Damage"]
                print("Your HP: %s" % character["Current HP"])
                print("Clown HP: %s" % clown_stats["Current HP"])
            else:
                print("\nWrong number!!!")
                character["Current HP"] = character["Current HP"] - clown_stats["Attack Damage"]
                print("You lost -2 HP for wrong number.")
                print("Your HP: %s" % character["Current HP"])
                print("Clown HP: %s" % clown_stats["Current HP"])


def final_boss(character):
    """
    Calls the finial boss to fight.

    :param character: a dictionary with x and y coordinates
    :return:
    """
    print("\nBattle")
    print("Fight the Monkey to death")
    monkey()
    monkey_stats = {"Current HP": 20, "Attack Damage": 5}

    monkey_dead = False
    while not monkey_dead:
        if monkey_stats["Current HP"] <= 0:
            print("congratulations %s you escaped the Gravestone Circus!" % character["Name"])
            firework()
            return True
        elif character["Current HP"] <= 0:
            dead()
            return True
        else:
            print("\nMoves\npunch: 1 kick: 2 run: 3 ")
            move = int(input("Enter move: "))

            if move == 1:
                monkey_stats["Current HP"] = monkey_stats["Current HP"] - character["Attack Damage"]
                character["Current HP"] = character["Current HP"] - monkey_stats["Attack Damage"]
                print("\nThe Monkey did 5 damage.")
                print("Your HP: %s" % character["Current HP"])
                print("You did %s damage" % character["Attack Damage"])
                print("Monkey HP: %s" % monkey_stats["Current HP"])
            elif move == 2:
                monkey_stats["Current HP"] = monkey_stats["Current HP"] - math.floor(character["Attack Damage"] * 0.8)
                character["Current HP"] = character["Current HP"] - monkey_stats["Attack Damage"]
                print("\nThe Monkey did 5 damage.")
                print("Your HP: %s" % character["Current HP"])
                print("You did %s damage" % math.floor(character["Attack Damage"] * 0.8))
                print("Monkey HP: %s" % monkey_stats["Current HP"])
            elif move == 3:
                print("\nYou can not run from the Boss!")
                print("You got attacked for trying to run -5 HP.")
                character["Current HP"] = character["Current HP"] - monkey_stats["Attack Damage"]
                print("Your HP: %s" % character["Current HP"])
                print("Monkey HP: %s" % monkey_stats["Current HP"])
            else:
                print("\nWrong number!!!")
                character["Current HP"] = character["Current HP"] - monkey_stats["Attack Damage"]
                print("You lost -5 HP for wrong number.")
                print("Your HP: %s" % character["Current HP"])
                print("Monkey HP: %s" % monkey_stats["Current HP"])


def dead():
    """
    Play the finial scene when the user dies.
    """
    print("\nyou fought a good fight.")
    death()
    print("GAME OVER")
    six_six = list(itertools.repeat(666, 6))
    for numbers in list(range(len(six_six))):
        print(six_six[numbers])


def game():  # called from main
    """
     Runs the game.

    """
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
        if direction == 'quit':
            print("You quit the game")
            achieved_goal = True
        valid_move = validate_move(character, direction)

        if valid_move:
            move_character(character, direction)
            there_is_a_challenge = check_for_quest(character, board)
            if there_is_a_challenge:
                health_check = execute_challenge_protocol(character)
                if health_check:
                    dead()
                    achieved_goal = True
            elif board[character["X-coordinate"], character["Y-coordinate"]] == "Boss":
                achieved_goal = final_boss(character)


def main():
    game()


if __name__ == "__main__":
    main()

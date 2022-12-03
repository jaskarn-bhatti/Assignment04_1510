"""
Jaskarn
Student number: A01328100
"""

from art import the_big_top


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
    user_stats = {"Name": user_name, "X-coordinate": 0, "Y-coordinate": 0, "Current HP": 10, "Attack Damage": 5}
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
    print("\nMove")
    print("West: w  North: n  East: e  South: s")
    movement_number = str(input("Enter direction: "))
    movement_number = movement_number.lower()
    if movement_number == 'w' or movement_number == 'n' or movement_number == 'e' or movement_number == 's':
        return movement_number
    else:
        print("Enter movement direction again")
        get_user_choice()


def game():  # called from main
    print("Gravestone Circus")
    the_big_top()
    print("April 13, 1990 you go out to watch magical monkey preform.")
    print("You arrive at the Circus to find yourself the only one in attendance.")
    print("As the show begins you see a big flash.")
    print("Your eyes open to realize that the exit is guarded by a giant monkey\n")
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
    # print(board)

    # Make character profile
    character = make_character(user_name)
    # print(character)

    achieved_goal = False
    while not achieved_goal:
        # Tell the user where they are
        describe_current_location(board, character)

        # 5
        direction = get_user_choice()
        # valid_move = validate_move(board, character, direction)
        # if valid_move:
        # move_character(character)
    # describe_current_location(board, character)
    # there_is_a_challenge = check_for_challenges()
    # if there_is_a_challenge:
    # execute_challenge_protocol(character)
    # if character_has_leveled():
    # execute_glow_up_protocol()
    # achieved_goal = check_if_goal_attained(board, character)
    # else:
    # # Tell the user they can’t go in that direction
    # # Print end of game stuff like congratulations or sorry you died
    #


def main():
    game()


if __name__ == "__main__":
    main()

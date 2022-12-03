"""
Jaskarn
Student number: A01328100
"""


from art import the_big_top

def make_board(rows, columns):
    a = {}
    for length in range(columns):
        for width in range(rows):
            a[length, width] = "Empty room"
    return a


def make_character(user_name):
    user_stats = {"Name": user_name, "X-coordinate": 0, "Y-coordinate": 0, "Current HP": 10, "Attack Damage": 5}
    return user_stats



def game():  # called from main
    print("Escape The Circus")
    the_big_top()
    print("Hello adventure")
    print("Enter your name: ")
    user_name = input()

    # makes board dictionary
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    print(board)

    # Make character profile
    character = make_character(user_name)
    print(character)

    achieved_goal = False
    while not achieved_goal:
    # Tell the user where they are
    describe_current_location(board, character)

    # 5
    # direction = get_user_choice( )
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

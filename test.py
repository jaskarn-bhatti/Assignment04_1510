def describe_current_location(board, character):
    character_pos = (character.get("X-coordinate"), character.get("Y-coordinate"))
    board_key = list(board.keys())
    current_board = []
    for size in range(len(board_key)):
        if character_pos == board_key[size]:
            current_board.append('0')
        elif board.get(board_key[size]) == "quest":
            current_board.append('Q')
        else:
            current_board.append('X')

    i = 0
    while i < 5:
        print(current_board[0:5])
        del current_board[0:5]
        i += 1

character = {'Name': 'jsas', 'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 10, 'Attack Damage': 5}
board = {(0, 0): 'Empty room', (0, 1): 'Empty room', (0, 2): 'Empty room', (0, 3): 'Empty room', (0, 4): 'Empty room', (1, 0): 'Empty room', (1, 1): 'quest', (1, 2): 'Empty room', (1, 3): 'Empty room', (1, 4): 'Empty room', (2, 0): 'Empty room', (2, 1): 'Empty room', (2, 2): 'Empty room', (2, 3): 'Empty room', (2, 4): 'Empty room', (3, 0): 'Empty room', (3, 1): 'Empty room', (3, 2): 'Empty room', (3, 3): 'Empty room', (3, 4): 'Empty room', (4, 0): 'Empty room', (4, 1): 'Empty room', (4, 2): 'quest', (4, 3): 'Empty room', (4, 4): 'Empty room'}
describe_current_location(board, character)
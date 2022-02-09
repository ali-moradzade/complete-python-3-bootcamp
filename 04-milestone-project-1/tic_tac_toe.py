def display_board(board):
    for row in board:
        for col in row:
            print("'{}'".format(col), end=' ')
        print()


def get_number():
    result = input("Enter a number between 1 and 9: ")
    while not result.isdigit():
        print("Invalid input (input must be a number). try again.\n")
        result = input("Enter a number between 1 and 9: ")

    return int(result)


def get_valid_number():
    digit = get_number()
    while digit < 1 or digit > 9:
        print('You should enter a number between 1 and 9! try again.\n')
        digit = get_number()

    return digit


def get_row_col(digit):
    row = (digit - 1) // 3
    col = (digit - 1) % 3
    return row, col


def check_empty_cell(board, digit):
    row, col = get_row_col(digit)
    return board[row][col].lower() not in ('x', 'o')


def get_user_input(board, turn):
    digit = get_valid_number()
    while not check_empty_cell(board, digit):
        print('The cell is not empty. try again.\n')
        digit = get_valid_number()

    row, col = get_row_col(digit)
    if turn == 1:
        board[row][col] = 'X'
    else:
        board[row][col] = 'O'


def is_winner(board, turn):
    if turn == 1:
        char = 'X'
    else:
        char = 'O'

    # Check horizontally
    for i in range(len(board)):
        if board[i] == [char, char, char]:
            return True

    # Check vertically
    for j in range(len(board[0])):
        if [board[0][j], board[1][j], board[2][j]] == [char, char, char]:
            return True

    # Check diagonals
    if [board[0][0], board[1][1], board[2][2]] == [char, char, char] or [board[0][2], board[1][1], board[2][0]] == [
        char, char, char]:
        return True

    return False


turn = 1
board = [['1', '2', '3'],
         ['4', '5', '6'],
         ['7', '8', '9']]

while True:
    display_board(board)
    print("Player {} turn.".format(turn))
    get_user_input(board, turn)

    if is_winner(board, turn):
        print()
        display_board(board)
        print('Congragulations! Player{} won the game!'.format(turn))
        break

    turn = 1 if turn == 2 else 2
    print()

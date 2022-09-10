import re
import os


# Link: https://www.geeksforgeeks.org/clear-screen-python/
def clear_screen():
	# for mac and linux(here, os.name is 'posix')
	if os.name == 'posix':
		_ = os.system('clear')
	else:
		# for windows platform
		_ = os.system('cls')


def display_board(board):
	clear_screen()
	for i in range(3):
		print('   |   |   ')
		print(' {} | {} | {} '.format(board[i][0], board[i][1], board[i][2]))
		print('   |   |   ')

		if (i + 1) != 3:
			print('-----------')


def get_number():
	result = input("Enter a number between 1 and 9: ")

	num_format = re.compile(r'^[-+]?\d+$')
	while not re.match(num_format, result):
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
		marker = 'X'
	else:
		marker = 'O'

	# Check horizontally
	for i in range(len(board)):
		if board[i] == [marker, marker, marker]:
			return True

	# Check vertically
	for j in range(len(board[0])):
		if [board[0][j], board[1][j], board[2][j]] == [marker, marker, marker]:
			return True

	# Check diagonals
	if [board[0][0], board[1][1], board[2][2]] == [marker, marker, marker] \
			or [board[0][2], board[1][1], board[2][0]] == [marker, marker, marker]:
		return True

	return False


def is_game_ended(board):
	for row in board:
		for col in row:
			if col not in ['X', 'O']:
				return False

	return True


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
		print('Congratulations! Player{} won the game!'.format(turn))
		break
	elif is_game_ended(board):
		print()
		display_board(board)
		print('No body won. game ended.')
		break

	turn = 1 if turn == 2 else 2
	print()

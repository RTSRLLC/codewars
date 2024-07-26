import numpy as np
import pandas as pd


def who_is_winner(pieces_position_list):
	print(f"{'=' * 50}\n")
	print(f"pieces_position_list: {pieces_position_list}")
	col_dict = {"A": [5, 0], "B": [5, 0], "C": [5, 0], "D": [5, 0], "E": [5, 0], "F": [5, 0], "G": [5, 0]}
	board = np.zeros((6, 7), dtype=object)
	pos_array = np.array([1, 2, 3, -1, 1, 2, -2, -1, 1, -3, -2, -1]).reshape(4, 3)
	pd_board = pd.DataFrame(board, columns=list('ABCDEFG'))
	for move, color in list(enumerate(pieces_position_list, start=1)):
		pd_board.at[col_dict[color[0]][0], color[0]] = color[2:]
		col_dict[color[0]][0] -= 1
		col_dict[color[0]][1] += 1
		if move >= 7:
			player = color[2:]
			row, col = col_dict[color[0]][0] + 1, list('ABCDEFG').index(color[0])
			print(f"row, col = {row}, {col}")
			pd_board.columns = list(range(7))
			
			row_indices = [('r', it) for item in (row + pos_array) for it in item]
			
			col_indices = [('c', it) for item in (col + pos_array) for it in item]
			
			############################################
			# check for winner in column
			try:
				if all(pd_board.iat[row, col] == pd_board.iat[abs(row - i), abs(col)] == player for i in range(1, 4)):
					print(f"Player: {player}, In check for winner in column row - i\nthe_board:\n{pd_board}")
					return player
			except IndexError:
				pass
			try:
				if all(pd_board.iat[row, col] == pd_board.iat[abs(row + i), abs(col)] == player for i in range(1, 4)):
					print(f"Player: {player}, In check for winner in column row + i\nthe_board:\n{pd_board}")
					return player
				else:
					pass
			except IndexError:
				pd_board.columns = list(col_dict.keys())
			############################################
			# check for winner in row
			try:
				if all(pd_board.iat[row, col] == pd_board.iat[abs(row), abs(col - i)] == player for i in range(1,4)) and len(pieces_position_list) != 42:
					print(f"Player: {player}, In check for winner in row col - i\nthe_board:\n{pd_board}")
					return player
			except IndexError:
				pass
			try:
				if all(pd_board.iat[row, col] == pd_board.iat[abs(row), abs(col + i)] == player for i in range(1, 4)):
					print(f"Player: {player}, In check for winner in row col + i\nthe_board:\n{pd_board}")
					return player
			except IndexError:
				pass
			############################################
			# check for winner in diagonal
			try:  # go left and down
				if all(
						pd_board.iat[row, col] == pd_board.iat[abs(row - i), abs(col - i)] == player for i in range(1, 4)
						) and len(pieces_position_list) != 42:
					print(f"Player: {player}, In check for winner in diagonal left and down]\nthe_board:\n{pd_board}")
					return player
			except IndexError:
				pass
			try:  # go left and up
				if all(
						pd_board.iat[row, col] == pd_board.iat[abs(row - i), abs(col + i)] == player for i in range(1, 4)
						) and len(pieces_position_list) != 42:
					print(f"Player: {player}, In check for winner in diagonal left and up\nthe_board:\n{pd_board}")
					return player
			except IndexError:
				pass
			try:  # go right and down
				if all(
						pd_board.iat[row, col] == pd_board.iat[abs(row + i), abs(col - i)] == player for i in range(1, 4)
						) and len(pieces_position_list) != 42:
					print(
						f"row and col = {row}, {col}\n"
						f"{[pd_board.iat[row, col]] + list(pd_board.iat[abs(row + i), abs(col - i)] for i in range(1, 4))}"
						)
					print(f"Player: {player}, In check for winner in diagonal right and down\nthe_board:\n{pd_board}")
					return player
			except IndexError:
				pass
			try:  # go right and up
				if all(pd_board.iat[row, col] == pd_board.iat[abs(row + i), abs(col + i)] == player for i in range(1, 4)):
					print(f"Player: {player}, In check for winner in diagonal right and up\nthe_board:\n{pd_board}")
					return player
			except IndexError:
				pd_board.columns = list(col_dict.keys())
		else:
			pd_board.columns = list(col_dict.keys())
		
	return 'Draw'

# make a numpy array with only the number 3
row = 3
col = 3

rows = np.array([1, 2, 3, -1, 1, 2, -2, -1, 1, -3, -2, -1]).reshape(4, 3)
# row_rows = row + rows
# col_rows = col + rows

# list_rows = row_rows.tolist()
test_row_indices = [('r', it) for item in (row + rows) for it in item]

# list_cols = col_rows.tolist()
test_col_indices = [('c', it) for item in (col + rows) for it in item]

# zip_list = list(zip(list_rows, list_cols))

e = who_is_winner(
	[
		"A_Red", "B_Yellow", "A_Red", "B_Yellow", "A_Red", "B_Yellow", "G_Red", "B_Yellow"
		]
	)  # , "Yellow")
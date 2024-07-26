import numpy as np
import pandas as pd


def who_is_winner(pieces_position_list):
	print(f"{'=' * 50}\n")
	print(f"pieces_position_list: {pieces_position_list}")
	col_dict = {"A": [5, 0], "B": [5, 0], "C": [5, 0], "D": [5, 0], "E": [5, 0], "F": [5, 0], "G": [5, 0]}
	board = np.zeros((6, 7), dtype=object)
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
			############################################
			# check for winner in diagonal
			try:  # go left and down
				if all(pd_board.iat[row, col] == pd_board.iat[abs(row - i), abs(col - i)] == player for i in range(1,4)) and len(pieces_position_list) != 42:
					print(f"Player: {player}, In check for winner in diagonal left and down]\nthe_board:\n{pd_board}")
					return player
			except IndexError:
				pass
			try:  # go left and up
				if all(pd_board.iat[row, col] == pd_board.iat[abs(row - i), abs(col + i)] == player for i in range(1,4)) and len(pieces_position_list) != 42:
					print(f"Player: {player}, In check for winner in diagonal left and up\nthe_board:\n{pd_board}")
					return player
			except IndexError:
				pass
			try:  # go right and down
				if all(pd_board.iat[row, col] == pd_board.iat[abs(row + i), abs(col - i)] == player for i in range(1,4)) and len(pieces_position_list) != 42:
					print(
						f"row and col = {row}, {col}\n"
						f"{[pd_board.iat[row, col]] + list(pd_board.iat[abs(row + i), abs(col - i)] for i in range(1, 4))}"
						)
					print(f"Player: {player}, In check for winner in diagonal right and down\nthe_board:\n{pd_board}")
					return player
			except IndexError:
				pass
			try:  # go right and up
				if all(pd_board.iat[row, col] == pd_board.iat[abs(row + i), abs(col + i)] == player for i in range(1,4)):
					print(f"Player: {player}, In check for winner in diagonal right and up\nthe_board:\n{pd_board}")
					return player
			except IndexError:
				pass
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
					pd_board.columns = list(col_dict.keys())
			except IndexError:
				pd_board.columns = list(col_dict.keys())
		else:
			pd_board.columns = list(col_dict.keys())
	return 'Draw'


# The grid is 6 row by 7 columns, those being named from A to G.
# You will receive a list of strings showing the order of the pieces which dropped in columns:
# The list may contain up to 42 moves and shows the order the players are playing.
# The first player who connects four items of the same color is the winner.
# You should return "Yellow", "Red" or "Draw" accordingly.
# Draw if the list ends and there is no winner.


# a = who_is_winner(
# 	[
# 		"C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red", "B_Yellow", "G_Red", "C_Yellow", "C_Red",
# 		"D_Yellow", "F_Red", "E_Yellow", "A_Red", "A_Yellow", "G_Red", "A_Yellow", "F_Red", "F_Yellow", "D_Red",
# 		"B_Yellow", "E_Red", "D_Yellow", "A_Red", "G_Yellow", "D_Red", "D_Yellow", "C_Red"
# 		]
# 	)  # , "Yellow"))
#
# b = who_is_winner(
# 	[
# 		"C_Yellow", "B_Red", "B_Yellow", "E_Red", "D_Yellow", "G_Red", "B_Yellow", "G_Red", "E_Yellow", "A_Red",
# 		"G_Yellow", "C_Red", "A_Yellow", "A_Red", "D_Yellow", "B_Red", "G_Yellow", "A_Red", "F_Yellow", "B_Red",
# 		"D_Yellow", "A_Red", "F_Yellow", "F_Red", "B_Yellow", "F_Red", "F_Yellow", "G_Red", "A_Yellow", "F_Red",
# 		"C_Yellow", "C_Red", "G_Yellow", "C_Red", "D_Yellow", "D_Red", "E_Yellow", "D_Red", "E_Yellow", "C_Red",
# 		"E_Yellow", "E_Red"
# 		]
# 	)  # , "Yellow")
#
# c = who_is_winner(
# 	[
# 		"F_Yellow", "G_Red", "D_Yellow", "C_Red", "A_Yellow", "A_Red", "E_Yellow", "D_Red", "D_Yellow", "F_Red",
# 		"B_Yellow", "E_Red", "C_Yellow", "D_Red", "F_Yellow", "D_Red", "D_Yellow", "F_Red", "G_Yellow", "C_Red",
# 		"F_Yellow", "E_Red", "A_Yellow", "A_Red", "C_Yellow", "B_Red", "E_Yellow", "C_Red", "E_Yellow", "G_Red",
# 		"A_Yellow", "A_Red", "G_Yellow", "C_Red", "B_Yellow", "E_Red", "F_Yellow", "G_Red", "G_Yellow", "B_Red",
# 		"B_Yellow", "B_Red"
# 		]
# 	)  # , "Red")
#
# d = who_is_winner(
# 	[
# 		"A_Yellow", "B_Red", "B_Yellow", "C_Red", "G_Yellow", "C_Red", "C_Yellow", "D_Red", "G_Yellow", "D_Red",
# 		"G_Yellow", "D_Red", "F_Yellow", "E_Red", "D_Yellow"
# 		]
# 	)  # , "Red")
#
e = who_is_winner(
	[
		"A_Red", "B_Yellow", "A_Red", "B_Yellow", "A_Red", "B_Yellow", "G_Red", "B_Yellow"
		]
	)  # , "Yellow")
#
# f = who_is_winner(
# 	[
# 		"A_Red", "B_Yellow", "A_Red", "E_Yellow", "F_Red", "G_Yellow", "A_Red", "G_Yellow"
# 		]
# 	)  # , "Draw")

# g = who_is_winner(
# 	[
# 		'B_Red', 'G_Yellow', 'D_Red', 'G_Yellow', 'E_Red', 'G_Yellow', 'C_Red', 'D_Yellow', 'B_Red', 'G_Yellow',
# 		'A_Red', 'A_Yellow', 'B_Red', 'C_Yellow', 'A_Red', 'B_Yellow', 'B_Red', 'D_Yellow', 'D_Red', 'A_Yellow',
# 		'E_Red', 'G_Yellow', 'G_Red']
# 	)  # , "Red")

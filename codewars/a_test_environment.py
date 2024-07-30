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
			pd_board.columns = list(range(7))
			
			# row possibilities
			try:
				if (pd_board.iat[row, col - 1] == player and
						pd_board.iat[row, col - 2] == player and pd_board.iat[row, col - 3] == player):
					print("row possibilities 1")
					print(pd_board.iat[row, col - 1], pd_board.iat[row, col - 2], pd_board.iat[row, col - 3], end="\n")
					return player
			except IndexError:
				pass
			try:
				if (pd_board.iat[row, col - 1] == player and
				      pd_board.iat[row, col - 2] == player and pd_board.iat[row, col + 1] == player):
					print("row possibilities 2")
					print(pd_board.iat[row, col - 1], pd_board.iat[row, col - 2], pd_board.iat[row, col + 1], end="\n")
					return player
			except IndexError:
				pass
			try:
				if (pd_board.iat[row, col - 1] == player and
				      pd_board.iat[row, col + 1] == player and pd_board.iat[row, col + 2] == player):
					print("row possibilities 3")
					print(pd_board.iat[row, col - 1], pd_board.iat[row, col + 1], pd_board.iat[row, col + 2], end="\n")
					return player
			except IndexError:
				pass
			try:
				if (pd_board.iat[row, col + 1] == player and
				      pd_board.iat[row, col + 2] == player and pd_board.iat[row, col + 3] == player):
					print("row possibilities 4")
					print(pd_board.iat[row, col + 1], pd_board.iat[row, col + 2], pd_board.iat[row, col + 3], end="\n")
					return player
			except IndexError:
				pass
			
			# column possibilities
			try:
				if (pd_board.iat[row - 1, col] == player and
				      pd_board.iat[row - 2, col] == player and pd_board.iat[row - 3, col] == player):
					print("column possibilities 1")
					print(pd_board.iat[row - 1, col], pd_board.iat[row - 2, col], pd_board.iat[row - 3, col], end="\n")
					return player
			except IndexError:
				pass
			try:
				if (pd_board.iat[row - 1, col] == player and
				      pd_board.iat[row + 1, col] == player and pd_board.iat[row + 2, col] == player):
					print("column possibilities 2")
					print(pd_board.iat[row - 1, col], pd_board.iat[row + 1, col], pd_board.iat[row + 2, col], end="\n")
					return player
			except IndexError:
				pass
			try:
				if (pd_board.iat[row - 1, col] == player and
				      pd_board.iat[row - 2, col] == player and pd_board.iat[row + 1, col] == player):
					print("column possibilities 3")
					print(pd_board.iat[row - 1, col], pd_board.iat[row - 2, col], pd_board.iat[row + 1, col], end="\n")
					return player
			except IndexError:
				pass
			try:
				if (pd_board.iat[row + 1, col] == player and
				      pd_board.iat[row + 2, col] == player and pd_board.iat[row + 3, col] == player):
					print("column possibilities 4")
					print(pd_board.iat[row + 1, col], pd_board.iat[row + 2, col], pd_board.iat[row + 3, col], end="\n")
					return player
			except IndexError:
				pass
			
			# diagonal possibilities negative slope
			try:
				if (pd_board.iat[row - 1, col - 1] == player and
				      pd_board.iat[row - 2, col - 2] == player and pd_board.iat[row - 3, col - 3] == player):
					print("diagonal possibilities negative slope 1")
					print(pd_board.iat[row - 1, col - 1], pd_board.iat[row - 2, col - 2], pd_board.iat[row - 3, col - 3], end="\n")
					return player
			except IndexError:
				pass
			try:
				if (pd_board.iat[row - 1, col - 1] == player and
				      pd_board.iat[row + 1, col + 1] == player and pd_board.iat[row + 2, col + 2] == player):
					print("diagonal possibilities negative slope 2")
					print(pd_board.iat[row - 1, col - 1], pd_board.iat[row + 1, col + 1], pd_board.iat[row + 2, col + 2], end="\n")
					return player
			except IndexError:
				pass
			try:
				if (pd_board.iat[row - 1, col - 1] == player and
				      pd_board.iat[row - 2, col - 2] == player and pd_board.iat[row + 1, col + 1] == player):
					print("diagonal possibilities negative slope 3")
					print(pd_board.iat[row - 1, col - 1], pd_board.iat[row - 2, col - 2], pd_board.iat[row + 1, col + 1], end="\n")
					return player
			except IndexError:
				pass
			try:
				if (pd_board.iat[row + 1, col + 1] == player and
				      pd_board.iat[row + 2, col + 2] == player and pd_board.iat[row + 3, col + 3] == player):
					print("diagonal possibilities negative slope 4")
					print(pd_board.iat[row + 1, col + 1], pd_board.iat[row + 2, col + 2], pd_board.iat[row + 3, col + 3], end="\n")
					return player
			except IndexError:
				pass
			
			# diagonal possibilities positive slope
			try:
				if (pd_board.iat[row - 1, col + 1] == player and
				      pd_board.iat[row - 2, col + 2] == player and pd_board.iat[row - 3, col + 3] == player):
					print("diagonal possibilities positive slope 1")
					print(pd_board.iat[row - 1, col + 1], pd_board.iat[row - 2, col + 2], pd_board.iat[row - 3, col + 3], end="\n")
					return player
			except IndexError:
				pass
			try:
				if (pd_board.iat[row + 1, col - 1] == player and
				      pd_board.iat[row - 1, col + 1] == player and pd_board.iat[row - 2, col + 2] == player):
					print("diagonal possibilities positive slope 2")
					print(pd_board.iat[row + 1, col - 1], pd_board.iat[row - 1, col + 1], pd_board.iat[row - 2, col + 2], end="\n")
					return player
			except IndexError:
				pass
			try:
				if (pd_board.iat[row + 1, col - 1] == player and
				      pd_board.iat[row + 2, col - 2] == player and pd_board.iat[row - 1, col + 1] == player):
					print("diagonal possibilities positive slope 3")
					print(pd_board.iat[row + 1, col - 1], pd_board.iat[row + 2, col - 2], pd_board.iat[row - 1, col + 1], end="\n")
					return player
			except IndexError:
				pass
			try:
				if (pd_board.iat[row + 1, abs(col - 1)] == player and
				      pd_board.iat[row + 2, col - 2] == player and pd_board.iat[row + 3, col - 3] == player):
					print("diagonal possibilities positive slope 4")
					print(pd_board.iat[row + 1, col - 1], pd_board.iat[row + 2, col - 2], pd_board.iat[row + 3, col - 3], end="\n")
					return player
				else:
					pd_board.columns = list(col_dict.keys())
			except IndexError:
				pd_board.columns = list(col_dict.keys())
	return "Draw"


a = who_is_winner(
	[
		"C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red", "B_Yellow", "G_Red", "C_Yellow", "C_Red",
		"D_Yellow", "F_Red", "E_Yellow", "A_Red", "A_Yellow", "G_Red", "A_Yellow", "F_Red", "F_Yellow", "D_Red",
		"B_Yellow", "E_Red", "D_Yellow", "A_Red", "G_Yellow", "D_Red", "D_Yellow", "C_Red"
		]
	)  # , "Yellow"))

b = who_is_winner(
	[
		"C_Yellow", "B_Red", "B_Yellow", "E_Red", "D_Yellow", "G_Red", "B_Yellow", "G_Red", "E_Yellow", "A_Red",
		"G_Yellow", "C_Red", "A_Yellow", "A_Red", "D_Yellow", "B_Red", "G_Yellow", "A_Red", "F_Yellow", "B_Red",
		"D_Yellow", "A_Red", "F_Yellow", "F_Red", "B_Yellow", "F_Red", "F_Yellow", "G_Red", "A_Yellow", "F_Red",
		"C_Yellow", "C_Red", "G_Yellow", "C_Red", "D_Yellow", "D_Red", "E_Yellow", "D_Red", "E_Yellow", "C_Red",
		"E_Yellow", "E_Red"
		]
	)  # , "Yellow")

c = who_is_winner(
	[
		"F_Yellow", "G_Red", "D_Yellow", "C_Red", "A_Yellow", "A_Red", "E_Yellow", "D_Red", "D_Yellow", "F_Red",
		"B_Yellow", "E_Red", "C_Yellow", "D_Red", "F_Yellow", "D_Red", "D_Yellow", "F_Red", "G_Yellow", "C_Red",
		"F_Yellow", "E_Red", "A_Yellow", "A_Red", "C_Yellow", "B_Red", "E_Yellow", "C_Red", "E_Yellow", "G_Red",
		"A_Yellow", "A_Red", "G_Yellow", "C_Red", "B_Yellow", "E_Red", "F_Yellow", "G_Red", "G_Yellow", "B_Red",
		"B_Yellow", "B_Red"
		]
	)  # , "Red")

d = who_is_winner(
	[
		"A_Yellow", "B_Red", "B_Yellow", "C_Red", "G_Yellow", "C_Red", "C_Yellow", "D_Red", "G_Yellow", "D_Red",
		"G_Yellow", "D_Red", "F_Yellow", "E_Red", "D_Yellow"
		]
	)  # , "Red")

e = who_is_winner(
	[
		"A_Red", "B_Yellow", "A_Red", "B_Yellow", "A_Red", "B_Yellow", "G_Red", "B_Yellow"
		]
	)  # , "Yellow")

f = who_is_winner(
	[
		"A_Red", "B_Yellow", "A_Red", "E_Yellow", "F_Red", "G_Yellow", "A_Red", "G_Yellow"
		]
	)  # , "Draw")

g = who_is_winner(
	[
		'B_Red', 'G_Yellow', 'D_Red', 'G_Yellow', 'E_Red', 'G_Yellow', 'C_Red', 'D_Yellow', 'B_Red', 'G_Yellow',
		'A_Red', 'A_Yellow', 'B_Red', 'C_Yellow', 'A_Red', 'B_Yellow', 'B_Red', 'D_Yellow', 'D_Red', 'A_Yellow',
		'E_Red', 'G_Yellow', 'G_Red']
	)  # , "Red")

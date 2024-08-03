import numpy as np
import pandas as pd
from collections import defaultdict, Counter


def who_is_winner(pieces_position_list):
	print(f"\n{'=' * 50}")
	print(f"len(pieces_position_list): {len(pieces_position_list)}\nactual list   {pieces_position_list}\n")
	col_dict = {"A": [5, 0], "B": [5, 0], "C": [5, 0], "D": [5, 0], "E": [5, 0], "F": [5, 0], "G": [5, 0]}
	board = np.empty((6, 7), dtype=object)
	pd_board = pd.DataFrame(board, columns=list('ABCDEFG'))
	# for user board visualization
	for move, color in list(enumerate(pieces_position_list, start=1)):
		pd_board.at[col_dict[color[0]][0], color[0]] = move, color
		col_dict[color[0]][0] -= 1
		col_dict[color[0]][1] += 1
		# winning move is: {'the_row_series': [(1, 'B_Red'), (7, 'C_Red'), (3, 'D_Red'), (5, 'E_Red'), (2, 'G_Yellow')]}
		if move >= 7:
			the_col_series = pd_board[color[0]].dropna().tolist()
			if len(the_col_series) >= 4:
				col_list_for_win = [i[1][2:] for i in the_col_series]
				count = 0
				for i in col_list_for_win:
					if i == color[2:]:
						count += 1
					else:
						count = 0
					if count == 4:
						return color[2:]
			the_row_series = pd_board[pd_board.apply(lambda row: row[color[0]] == (move, color), axis=1)].iloc[0].dropna().tolist()
			if len(the_row_series) >= 4:
				row_list_for_win = [i[1][2:] for i in the_row_series]
				count = 0
				for i in row_list_for_win:
					if i == color[2:]:
						count += 1
					else:
						count = 0
					if count == 4:
						return color[2:]
			for i in range(-5, 5):
				the_diagonal_series = pd.Series(pd_board.to_numpy().diagonal(offset=i)).dropna().tolist()
				if (move, color) in the_diagonal_series and len(the_diagonal_series) >= 4:
					diagonal_list_for_win = [i[1][2:] for i in the_diagonal_series]
					count = 0
					for i in diagonal_list_for_win:
						if i == color[2:]:
							count += 1
						else:
							count = 0
						if count == 4:
							return color[2:]
	
	return "Draw"


a = who_is_winner(
	[
		"C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red", "B_Yellow", "G_Red", "C_Yellow", "C_Red",
		"D_Yellow", "F_Red", "E_Yellow", "A_Red", "A_Yellow", "G_Red", "A_Yellow", "F_Red", "F_Yellow", "D_Red",
		"B_Yellow", "E_Red", "D_Yellow", "A_Red", "G_Yellow", "D_Red", "D_Yellow", "C_Red"
		]
	)  # , "Yellow"))
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
# e = who_is_winner(
# 	[
# 		"A_Red", "B_Yellow", "A_Red", "B_Yellow", "A_Red", "B_Yellow", "G_Red", "B_Yellow"
# 		]
# 	)  # , "Yellow")
#
# f = who_is_winner(
# 	[
# 		"A_Red", "B_Yellow", "A_Red", "E_Yellow", "F_Red", "G_Yellow", "A_Red", "G_Yellow"
# 		]
# 	)  # , "Draw")
#
# g = who_is_winner(
# 	[
# 		'B_Red', 'G_Yellow', 'D_Red', 'G_Yellow', 'E_Red', 'G_Yellow', 'C_Red', 'D_Yellow', 'B_Red', 'G_Yellow',
# 		'A_Red', 'A_Yellow', 'B_Red', 'C_Yellow', 'A_Red', 'B_Yellow', 'B_Red', 'D_Yellow', 'D_Red', 'A_Yellow',
# 		'E_Red', 'G_Yellow', 'G_Red']
# 	)  # , "Red")
#
# h = who_is_winner(
# 	['B_Red', 'A_Yellow', 'C_Red', 'E_Yellow', 'A_Red', 'C_Yellow', 'E_Red', 'A_Yellow', 'D_Red', 'C_Yellow', 'C_Red',
# 	 'D_Yellow', 'G_Red', 'G_Yellow', 'C_Red', 'B_Yellow', 'C_Red']
# 	)  # , "Draw")
#
# i = who_is_winner(
# 	['B_Red', 'D_Yellow', 'C_Red', 'E_Yellow', 'C_Red', 'G_Yellow', 'B_Red', 'B_Yellow', 'B_Red', 'B_Yellow', 'F_Red',
# 	 'E_Yellow', 'E_Red', 'G_Yellow', 'A_Red', 'G_Yellow', 'D_Red', 'C_Yellow', 'B_Red'])  # Draw

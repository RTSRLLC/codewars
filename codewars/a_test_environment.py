import numpy as np
import pandas as pd
from collections import defaultdict, Counter

def who_is_winner(pieces_position_list):
	print(f"\n{'=' * 50}")
	print(f"len(pieces_position_list): {len(pieces_position_list)}\nactual list   {pieces_position_list}\n")
	col_dict = {"A": [5, 0], "B": [5, 0], "C": [5, 0], "D": [5, 0], "E": [5, 0], "F": [5, 0], "G": [5, 0]}
	board = np.zeros((6, 7), dtype=object)
	pd_board = pd.DataFrame(board, columns=list('ABCDEFG'))
	# for user board visualization
	for move, color in list(enumerate(pieces_position_list, start=1)):
		pd_board.at[col_dict[color[0]][0], color[0]] = move, color
		col_dict[color[0]][0] -= 1
		col_dict[color[0]][1] += 1
		# if move >= 7:
	# ================================
	# test various sorting methods on pieces_position_list
	# could be good for column checks
	on_x0 = sorted(pieces_position_list, key=lambda x: x[0])
	count_x0 = Counter(on_x0)
	greater_then_4 = [k[0] for k, v in count_x0.items() if v >= 4]
	# get items in board_array_transposed that are in greater_then_4
	pd_board.columns = list(col_dict.keys())
	possible_winning_rows = [(row, tuple(col)) for row, col in pd_board.T.iterrows() if row in greater_then_4]
	print("possible_winning_rows")
	the_min = None
	for item in possible_winning_rows:
		zero = item[0]
		one = item[1]
		ending = item[1][1:]
		print(min(i[0] for i in item[1][1:]))
		the_min = min(i[0] for i in item[1][1:])
		if the_min < the_min:
			print(the_min)
			the_min = the_min

	

	
	return "Draw"


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
g = who_is_winner(
	[
		'B_Red', 'G_Yellow', 'D_Red', 'G_Yellow', 'E_Red', 'G_Yellow', 'C_Red', 'D_Yellow', 'B_Red', 'G_Yellow',
		'A_Red', 'A_Yellow', 'B_Red', 'C_Yellow', 'A_Red', 'B_Yellow', 'B_Red', 'D_Yellow', 'D_Red', 'A_Yellow',
		'E_Red', 'G_Yellow', 'G_Red']
	)  # , "Red")
#
# h = who_is_winner(
# 	['B_Red', 'A_Yellow', 'C_Red', 'E_Yellow', 'A_Red', 'C_Yellow', 'E_Red', 'A_Yellow', 'D_Red', 'C_Yellow', 'C_Red',
# 	 'D_Yellow', 'G_Red', 'G_Yellow', 'C_Red', 'B_Yellow', 'C_Red']
# 	)  # , "Draw")
#
# i = who_is_winner(
# 	['B_Red', 'D_Yellow', 'C_Red', 'E_Yellow', 'C_Red', 'G_Yellow', 'B_Red', 'B_Yellow', 'B_Red', 'B_Yellow', 'F_Red',
# 	 'E_Yellow', 'E_Red', 'G_Yellow', 'A_Red', 'G_Yellow', 'D_Red', 'C_Yellow', 'B_Red'])  # Draw

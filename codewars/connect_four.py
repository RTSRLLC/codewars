import numpy as np
import pandas as pd


def who_is_winner(pieces_position_list):
	col_dict = {"A": [6, 0], "B": [6, 0], "C": [6, 0], "D": [6, 0], "E": [6, 0], "F": [6, 0], "G": [6, 0]}
	board = np.zeros((6, 7), dtype=object)
	pd_board = pd.DataFrame(board, index=[1, 2, 3, 4, 5, 6], columns=list(col_dict.keys()))
	for move, color in list(enumerate(pieces_position_list, start=1)):
		pd_board.at[col_dict[color[0]][0], color[0]] = color[2]
		col_dict[color[0]][0] -= 1
		col_dict[color[0]][1] += 1
		if move >= 7:
			player = color[2]
			row, col = col_dict[color[0]][0] + 1, color[0]
			the_row = pd_board.loc[row]
			the_row.reset_index(drop=True, inplace=True)
			
			test_row_minus_4 = the_row.iloc[row:row-4:-1]
			row_minus_4 = all(the_row.iloc[row:row-4:-1])
			test_row_plus_4 = the_row.iloc[row:row+4]
			row_plus_4 = all(the_row.iloc[row:row+4])
			
			the_col = pd_board[col]
			
			
			transposed = pd_board.T
			print(transposed)
	return None


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

f = who_is_winner(
	[
		"A_Red", "B_Yellow", "A_Red", "E_Yellow", "F_Red", "G_Yellow", "A_Red", "G_Yellow"
		]
	)  # , "Draw")

# def visualize_board(board: dict) -> np.array:
# 	max_length = max([len(i) for i in board.values()])
# 	for i in board.values():
# 		if len(i) < max_length:
# 			i.extend([0] * (max_length - len(i)))
# 	np_values = np.transpose(np.array(list(board.values())))
# 	return np_values
#
#
# def check_consecutive(arr, num=4):
# 	# Check rows and columns
# 	for row in arr:
# 		if check_sequence(row, num):
# 			return row
# 	for col in arr.T:
# 		if check_sequence(col, num):
# 			return col
#
# 	# Check diagonals
# 	for offset in range(-arr.shape[0] + 1, arr.shape[1]):
# 		if check_sequence(arr.diagonal(offset), num):
# 			return arr.diagonal(offset)
# 		if check_sequence(np.fliplr(arr).diagonal(offset), num):
# 			return np.fliplr(arr).diagonal(offset)
#
# 	return False
#
#
# def check_sequence(seq, num):
# 	count = 1
# 	for i in range(1, len(seq)):
# 		if seq[i] == seq[i - 1] and seq[i] != 0:
# 			count += 1
# 			if count == num:
# 				return True
# 		else:
# 			count = 1
# 	return False
#
#
# def who_is_winner(pieces_position_list):
# 	column_dict = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': []}
# 	color_coding = {'Red': 1, 'Yellow': 2}
# 	reverse_color_coding = {v: k for k, v in color_coding.items()}
# 	for color in pieces_position_list:
# 		column_dict[color[0]].append(color_coding[color[2:]])
# 	np_board = visualize_board(column_dict)
# 	print(f"np_board: \n{np_board}")
# 	try:
# 		check_winner = list(check_consecutive(np_board))
# 	except TypeError:
# 		return 'Draw'
# 	print(f"Winner: {check_winner}, check_winner[0]: {check_winner[0]} is  {reverse_color_coding[check_winner[0]]}")
#
# 	return reverse_color_coding[check_winner[0]]

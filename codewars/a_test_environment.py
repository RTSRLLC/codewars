import numpy as np
import pandas as pd


def the_counting_list(a_list, colr=None):
	count = 0
	for i in a_list:
		if i == colr:
			count += 1
		else:
			count = 0
		if count == 4:
			return colr
	return None


def diagonal(df, mv=None, colr=None):
	for i in range(-5, 5):
		the_diagonal_series_transpose = pd.Series(df.to_numpy().T.diagonal(offset=i)).tolist()
		if (mv, colr) in the_diagonal_series_transpose and len(the_diagonal_series_transpose) >= 4:
			diagonal_transpose_list_for_win = [i[1][2:] for i in the_diagonal_series_transpose]
			dia_count = the_counting_list(diagonal_transpose_list_for_win, colr[2:])
			if dia_count is not None:
				return dia_count
	return None


def who_is_winner(pieces_position_list: list) -> str:
	# provide a countdown for each column in order to place the pieces for user visualization
	col_dict = {"A": [5, 0], "B": [5, 0], "C": [5, 0], "D": [5, 0], "E": [5, 0], "F": [5, 0], "G": [5, 0]}
	
	# for user board visualization and ensure all cells are tuples for later code
	# create numpy array and convert to pandas DataFrame amking the numbers string tuples.
	board = np.ones((6, 7), dtype=object) * 10
	pd_board = pd.DataFrame(board, columns=list('ABCDEFG')).applymap(lambda x: tuple(str(x)))
	
	# Place each piece on the board
	for move, color in list(enumerate(pieces_position_list, start=1)):
		# a tuple with move is needed to ensure the number of moves is not lost
		pd_board.at[col_dict[color[0]][0], color[0]] = move, color  # a tuple to match the existing board
		col_dict[color[0]][0] -= 1
		col_dict[color[0]][1] += 1
		
		# check for winning conditions if there are at least 7 moves, the min for a win
		if move >= 7:
			# check current column for a win
			the_col_series = pd_board[color[0]].tolist()
			if len(the_col_series) >= 4:  # at least 4 needed to win
				col_list_for_win = [i[1][2:] for i in the_col_series]  # put the col elements in a list
				col_count = the_counting_list(col_list_for_win, color[2:])  # check for a win or None if not
				if col_count is not None:
					return col_count
				
			# check current row for a win
			the_row_series = (
				pd_board[pd_board.apply(lambda row: row[color[0]] == (move, color), axis=1)].iloc[0].tolist())
			if len(the_row_series) >= 4:  # at least 4 needed to win
				row_list_for_win = [i[1][2:] for i in the_row_series]  # put the row elements in a list
				row_count = the_counting_list(row_list_for_win, color[2:])  # check for a win or None if not
				if row_count is not None:
					return row_count
			
			# check negative (left to right top to bottom) diagonals for a win
			reg = diagonal(pd_board, mv=move, colr=color)
			if reg is not None:
				return diagonal(pd_board, mv=move, colr=color)
			
			# check positive (right to left top to bottom) diagonals for a win but flipped it for np.diagonal() reqs
			reg_flip = diagonal(pd_board.iloc[:, ::-1], mv=move, colr=color)
			if reg_flip is not None:
				return diagonal(pd_board.iloc[:, ::-1], mv=move, colr=color)
			
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

h = who_is_winner(
	['B_Red', 'A_Yellow', 'C_Red', 'E_Yellow', 'A_Red', 'C_Yellow', 'E_Red', 'A_Yellow', 'D_Red', 'C_Yellow', 'C_Red',
	 'D_Yellow', 'G_Red', 'G_Yellow', 'C_Red', 'B_Yellow', 'C_Red']
	)  # , "Draw")

i = who_is_winner(
	['B_Red', 'D_Yellow', 'C_Red', 'E_Yellow', 'C_Red', 'G_Yellow', 'B_Red', 'B_Yellow', 'B_Red', 'B_Yellow', 'F_Red',
	 'E_Yellow', 'E_Red', 'G_Yellow', 'A_Red', 'G_Yellow', 'D_Red', 'C_Yellow', 'B_Red']
	)  # Draw

j = who_is_winner(
	['A_Yellow', 'B_Red', 'B_Yellow', 'C_Red', 'G_Yellow', 'C_Red', 'C_Yellow', 'D_Red', 'G_Yellow', 'D_Red',
	 'G_Yellow', 'D_Red', 'F_Yellow', 'E_Red', 'D_Yellow']
	)

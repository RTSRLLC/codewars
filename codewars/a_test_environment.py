import numpy as np
import pandas as pd
from typing import Optional


def the_counting_list(a_list: list, colr=None) -> Optional[str]:
	"""
	Counts consecutive occurrences of a specified element in a list.

	This function iterates through a list and counts consecutive occurrences of a specified element.
	If the element appears four times consecutively, the function returns that element. Otherwise, it returns None.

	Parameters:
	a_list (list): The list in which to count consecutive occurrences.
	colr (str, optional): The element to count consecutive occurrences of. Defaults to None.

	Returns:
	Optional[str]: The element if it appears four times consecutively, otherwise None.
	"""
	count = 0
	for i in a_list:
		if i == colr:
			count += 1
		else:
			count = 0
		if count == 4:
			return colr
	return None


def diagonal(df: pd.DataFrame, *, mv: int = None, colr: str = None) -> Optional[str]:
	"""
	Checks for consecutive occurrences of a specified element in the diagonals of a DataFrame.

	This function iterates through the diagonals of a DataFrame and checks for consecutive occurrences
	of a specified element. If the element appears four times consecutively in any diagonal, the function
	returns that element. Otherwise, it returns None.

	Parameters:
	df (pd.DataFrame): The DataFrame in which to check the diagonals.
	mv (int, optional): The move number associated with the element. Defaults to None.
	colr (str, optional): The element to check for consecutive occurrences. Defaults to None.

	Returns:
	Optional[str]: The element if it appears four times consecutively in any diagonal, otherwise None.
	"""
	for _ in range(-5, 5):
		the_diagonal_series_transpose = pd.Series(df.to_numpy().T.diagonal(offset=_)).tolist()
		if (mv, colr) in the_diagonal_series_transpose:
			diagonal_transpose_list_for_win = [i[1][2:] for i in the_diagonal_series_transpose]
			dia_count = the_counting_list(diagonal_transpose_list_for_win, colr[2:])
			if dia_count is not None:
				return dia_count
	return None


def who_is_winner(pieces_position_list: list) -> str:
	"""
	Determines the winner of a Connect Four game based on the sequence of moves.

	This function simulates a Connect Four game by placing pieces on a board according to the given sequence of moves.
	It checks for a winner after each move, and if a player gets four consecutive pieces in a row, column, or diagonal,
	the function returns the color of the winning player. If no player wins after all moves, it returns "Draw".

	Parameters:
	pieces_position_list (list): A list of strings representing the moves in the game. Each string is in the format
								 "Column_Color", where Column is a letter from 'A' to 'G' and Color is either "Red" or "Yellow".

	Returns:
	str: The color of the winning player ("Red" or "Yellow") if there is a winner, otherwise "Draw".
	"""
	# provide a countdown for each column in order to place the pieces for user visualization
	col_dict = {"A": [5, 0], "B": [5, 0], "C": [5, 0], "D": [5, 0], "E": [5, 0], "F": [5, 0], "G": [5, 0]}
	
	# for user board visualization and ensure all cells are tuples for later code
	# create numpy array and convert to pandas DataFrame making the numbers string tuples.
	board = np.ones((6, 7), dtype=object) * 10
	pd_board = pd.DataFrame(board, columns=list('ABCDEFG')).apply(lambda x: x.map(lambda y: tuple(str(y))))
	
	# Place each piece on the board
	for move, color in enumerate(pieces_position_list, start=1):
		# a tuple with move is needed to ensure the number of moves is not lost
		pd_board.at[col_dict[color[0]][0], color[0]] = move, color  # a tuple to match the existing board
		col_dict[color[0]][0] -= 1
		col_dict[color[0]][1] += 1
		
		# check for winning conditions if there are at least 7 moves, the min for a win
		if move >= 7:
			
			# Extract the current column, row, and diagonal series
			the_col_series = pd_board[color[0]].tolist()
			the_row_series = (
				pd_board[pd_board.apply(lambda row: row[color[0]] == (move, color), axis=1)].iloc[0].tolist())
			reg = diagonal(
				pd_board, mv=move, colr=color
				)  # check negative (left to right top to bottom) diagonals for a win
			reg_flip = diagonal(
				pd_board.iloc[:, ::-1], mv=move, colr=color
				)  # check positive (right to left top to bottom) diagonals for win. Flipped it for np.diagonal() reqs
			
			# check current column for a win
			col_list_for_win = [i[1][2:] for i in the_col_series]  # put the col elements in a list
			col_count = the_counting_list(col_list_for_win, color[2:])  # check for a win or None if not
			if col_count is not None:
				return col_count
			
			# check current row for a win
			row_list_for_win = [i[1][2:] for i in the_row_series]  # put the row elements in a list
			row_count = the_counting_list(row_list_for_win, color[2:])  # check for a win or None if not
			if row_count is not None:
				return row_count
			
			# check both diagonals for a win
			if reg is not None:
				return reg
			if reg_flip is not None:
				return reg_flip
	
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

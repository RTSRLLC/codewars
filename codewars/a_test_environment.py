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
			area_check = pd_board.iloc[row - 1:row + 2, col - 1:col + 2]
			# Find the row and column indices of the player in the area_check DataFrame
			bool_df = area_check.eq(player)
			stacked_bool_df = bool_df.stack()
			
			matching_indices = stacked_bool_df[stacked_bool_df]
			if len(matching_indices) > 1:
				rows = list(matching_indices.index.get_level_values(0))
				rows_equal = all(i == rows[0] for i in rows)
				cols = list(matching_indices.index.get_level_values(1))
				cols_equal = all(i == cols[0] for i in cols)
				# establish the direction of the possible winning streak and get new df indices.
				if rows_equal is False or cols_equal is False:
					if not rows_equal:
						print(f'not rows_equal: {rows}')
						row_indices_positive = [0 if num < 0 else num for num in [rows[0], rows[0] + 3]]
						row_indices_negative = [0 if num < 0 else num for num in [rows[0] - 3, rows[0]]]
						print(f'row_indices_positive: {row_indices_positive}\nrow_indices_negative: {row_indices_negative}')
					else:
						row_indices_positive = rows
						print(f'row_indices_positive: {row_indices_positive}')
					if not cols_equal:
						print(f'not cols_equal: {cols}')
						col_indices_positive = [0 if num < 0 else num for num in [cols[0], cols[0] + 3]]
						col_indices_negative = [0 if num < 0 else num for num in [cols[0] - 3, cols[0]]]
						print(f'col_indices_positive: {col_indices_positive}\ncol_indices_negative: {col_indices_negative}')
					else:
						col_indices_positive = cols
						print(f'col_indices_positive: {col_indices_positive}')
					pd_board_streak_positive = pd_board.iloc[row_indices_positive[0]:row_indices_positive[1] + 1, col_indices_positive[0]:col_indices_positive[1] + 1]
					print(f"pd_board_streak_positive:\n{pd_board_streak_positive}")
					if all(pd_board_streak_positive.eq(player)):
						print(f"Player: {player}, In check for winner in streak positive\nthe_board:\n{pd_board}")
						return player
			pd_board.columns = list(col_dict.keys())
			print()
	
	return 'Draw'


e = who_is_winner(
	[
		"A_Red", "B_Yellow", "A_Red", "B_Yellow", "A_Red", "B_Yellow", "G_Red", "B_Yellow"
		]
	)  # , "Yellow")
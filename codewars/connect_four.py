import numpy as np
import pandas as pd

def who_is_winner(pieces_position_list):
	# final dict entries are row number, color,
	# associate the column letter with its number
	column_dict = {
		'A': [f"1 {i[2]}" for i in pieces_position_list if i[0] == 'A'],
		'B': [f"2 {i[2]}" for i in pieces_position_list if i[0] == 'B'],
		'C': [f"3 {i[2]}" for i in pieces_position_list if i[0] == 'C'],
		'D': [f"4 {i[2]}" for i in pieces_position_list if i[0] == 'D'],
		'E': [f"5 {i[2]}" for i in pieces_position_list if i[0] == 'E'],
		'F': [f"6 {i[2]}" for i in pieces_position_list if i[0] == 'F'],
		'G': [f"7 {i[2]}" for i in pieces_position_list if i[0] == 'G']
		}
	
	longest = max([len(i) for i in column_dict.values()])
	for key, val in column_dict.items():
		counter = 0
		for i in val:
			split = i.split()
			if split[1] == "R":
				split[1] = '7'
			elif split[1] == "Y":
				split[1] = '8'
			val[counter] = int(''.join(split) + str(counter))
			counter += 1
		column_dict[key] = val
		counter = 0
		
	values_flattened = [val for sublist in column_dict.values() for val in sublist]
	
	return None


# The grid is 6 row by 7 columns, those being named from A to G.
# You will receive a list of strings showing the order of the pieces which dropped in columns:
# The list may contain up to 42 moves and shows the order the players are playing.
# The first player who connects four items of the same color is the winner.
# You should return "Yellow", "Red" or "Draw" accordingly.
# Draw if the list ends and there is no winner.

# A,B,C,D,E,F,G are the columns and 1,2,3,4,5,6 are the rows.

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

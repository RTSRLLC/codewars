from itertools import permutations
import time
from typing import Any, Generator

start_time = time.time()

ELEMENTS = {
	'H': 'Hydrogen', 'He': 'Helium', 'Li': 'Lithium', 'Be': 'Beryllium', 'B': 'Boron', 'C': 'Carbon', 'N': 'Nitrogen', 'O': 'Oxygen', 'F': 'Fluorine',
	'Ne': 'Neon', 'Na': 'Sodium', 'Mg': 'Magnesium', 'Al': 'Aluminium', 'Si': 'Silicon', 'P': 'Phosphorus', 'S': 'Sulfur', 'Cl': 'Chlorine', 'Ar': 'Argon',
	'K': 'Potassium', 'Ca': 'Calcium', 'Sc': 'Scandium', 'Ti': 'Titanium', 'V': 'Vanadium', 'Cr': 'Chromium', 'Mn': 'Manganese', 'Fe': 'Iron', 'Co': 'Cobalt',
	'Ni': 'Nickel', 'Cu': 'Copper', 'Zn': 'Zinc', 'Ga': 'Gallium', 'Ge': 'Germanium', 'As': 'Arsenic', 'Se': 'Selenium', 'Br': 'Bromine', 'Kr': 'Krypton',
	'Rb': 'Rubidium', 'Sr': 'Strontium', 'Y': 'Yttrium', 'Zr': 'Zirconium', 'Nb': 'Niobium', 'Mo': 'Molybdenum', 'Tc': 'Technetium', 'Ru': 'Ruthenium',
	'Rh': 'Rhodium', 'Pd': 'Palladium', 'Ag': 'Silver', 'Cd': 'Cadmium', 'In': 'Indium', 'Sn': 'Tin', 'Sb': 'Antimony', 'Te': 'Tellurium', 'I': 'Iodine',
	'Xe': 'Xenon', 'Cs': 'Caesium', 'Ba': 'Barium', 'La': 'Lanthanum', 'Ce': 'Cerium', 'Pr': 'Praseodymium', 'Nd': 'Neodymium', 'Pm': 'Promethium',
	'Sm': 'Samarium', 'Eu': 'Europium', 'Gd': 'Gadolinium', 'Tb': 'Terbium', 'Dy': 'Dysprosium', 'Ho': 'Holmium', 'Er': 'Erbium', 'Tm': 'Thulium',
	'Yb': 'Ytterbium', 'Lu': 'Lutetium', 'Hf': 'Hafnium', 'Ta': 'Tantalum', 'W': 'Tungsten', 'Re': 'Rhenium', 'Os': 'Osmium', 'Ir': 'Iridium',
	'Pt': 'Platinum',
	'Au': 'Gold', 'Hg': 'Mercury', 'Tl': 'Thallium', 'Pb': 'Lead', 'Bi': 'Bismuth', 'Po': 'Polonium', 'At': 'Astatine', 'Rn': 'Radon', 'Fr': 'Francium',
	'Ra': 'Radium', 'Ac': 'Actinium', 'Th': 'Thorium', 'Pa': 'Protactinium', 'U': 'Uranium', 'Np': 'Neptunium', 'Pu': 'Plutonium', 'Am': 'Americium',
	'Cm': 'Curium', 'Bk': 'Berkelium', 'Cf': 'Californium', 'Es': 'Einsteinium', 'Fm': 'Fermium', 'Md': 'Mendelevium', 'No': 'Nobelium', 'Lr': 'Lawrencium',
	'Rf': 'Rutherfordium', 'Db': 'Dubnium', 'Sg': 'Seaborgium', 'Bh': 'Bohrium', 'Hs': 'Hassium', 'Mt': 'Meitnerium', 'Ds': 'Darmstadtium',
	'Rg': 'Roentgenium',
	'Cn': 'Copernicium', 'Uut': 'Ununtrium', 'Fl': 'Flerovium', 'Uup': 'Ununpentium', 'Lv': 'Livermorium', 'Uus': 'Ununseptium', 'Uuo': 'Ununoctium'
	}


def elemental_forms(word: str) -> list:
	"""
	Determines all possible combinations of element symbols that can form the given word.

	This function attempts to match the input word with valid chemical element symbols
	from the periodic table, considering single, double, and triple character symbols.

	Args:
		word (str): The word to be analyzed for possible element symbol combinations.

	Returns:
		list: A list of lists, where each inner list contains strings representing
			  a valid combination of element names and their symbols that can form the word.
			  If the word is empty, an empty list is returned.
	"""
	if word == '':
		return []

	results = []

	def find_combinations(current_pos, current_combination):

		"""
		Recursively finds all possible combinations of element symbols that can form the given word.

		This helper function attempts to match segments of the input word with valid chemical element symbols
		from the periodic table, considering single, double, and triple character symbols.

		Args:
			current_pos (int): The current position in the word being analyzed.
			current_combination (list): The current list of element names and symbols forming part of the word.

		Returns:
			None: The function appends valid combinations to the `results` list defined in the outer scope.
		"""
		# Base case: if we reach the end of the word
		if current_pos >= len(word):
			results.append(current_combination.copy())
			return

		# single-character elements
		single_letter = word[current_pos].upper()
		if single_letter in ELEMENTS:
			find_combinations(current_pos + 1, current_combination + [f"{ELEMENTS[single_letter]} ({single_letter})"])

		# two-character elements
		if current_pos + 1 < len(word):
			double_letter = word[current_pos:current_pos + 2].capitalize()
			if double_letter in ELEMENTS:
				find_combinations(current_pos + 2, current_combination + [f"{ELEMENTS[double_letter]} ({double_letter})"])

		# three-character elements
		if current_pos + 2 < len(word):
			triple_letter = word[current_pos:current_pos + 3].capitalize()
			if triple_letter in ELEMENTS:
				find_combinations(current_pos + 3, current_combination + [f"{ELEMENTS[triple_letter]} ({triple_letter})"])

	find_combinations(0, [])
	return results


a = elemental_forms('snack')
sorted_a = sorted(a)
answer = sorted(
	[
		['Sulfur (S)', 'Nitrogen (N)', 'Actinium (Ac)', 'Potassium (K)'],
		['Sulfur (S)', 'Sodium (Na)', 'Carbon (C)', 'Potassium (K)'],
		['Tin (Sn)', 'Actinium (Ac)', 'Potassium (K)']
		]
	)
# print(f"Test case a: {answer == sorted_a=}")
#
# b = elemental_forms('beach')
# sorted_b = sorted(b)
# answer_b = sorted([['Beryllium (Be)', 'Actinium (Ac)', 'Hydrogen (H)']])
# print('Test case b:', answer_b == sorted_b)
#
# c = elemental_forms('BEACH')
# sorted_c = sorted(c)
# answer_c = sorted([['Beryllium (Be)', 'Actinium (Ac)', 'Hydrogen (H)']])
# print('Test case c:', sorted_c == answer_c)
#
# d = elemental_forms('')
#
# end_time = time.time()
# print(f'Execution time: {(end_time - start_time) * 1000} milliseconds')

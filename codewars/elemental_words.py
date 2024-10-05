from typing import List

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


def check_symbol(symbol: str):
	return ELEMENTS.get(symbol, 'Invalid symbol')


def elemental_forms(word: str) -> List[List[str]]:
	
	def reset_doubles() -> None:
		"""
		This function resets the internal state of the elemental_forms function for processing double letter elements.
	
		Parameters:
		None
	
		Returns:
		None
	
		This function is a helper function for the elemental_forms function. It is used to reset the list_word, length, and list_word_iter variables to their
		initial state. This is necessary because the elemental_forms function processes the input word in multiple passes, and the state of these variables
		needs to be preserved between passes.
		"""
		nonlocal list_word, length, list_word_iter
		list_word = list(word.upper())
		length = len(word)
		list_word_iter = iter(list_word)
	
	elements_are = list()
	length = len(word)
	list_word = list(word.upper())
	
	# check dict for single upper letter elements
	elements_are.append(
		[f"{check_symbol(i)} ({i})" for i in list_word if not f"{check_symbol(i)} ({i})".startswith('Invalid symbol')]
		)
	
	# permutations for 2 letter elements
	list_word_iter = iter(list_word)
	add_list = []
	for let in list_word:
		while length:
			try:
				form_letter = ''.join(let + next(list_word_iter).lower())
				add_list.append(
					f"{check_symbol(form_letter)} ({form_letter})" if ELEMENTS.get(form_letter, 'Invalid symbol') != 'Invalid symbol' else ''
					)
				length -= 1
			except StopIteration:
				reset_doubles()
		reset_doubles()
	elements_are.append(add_list)
	
	# permutations for 3 letter elements
	three_letter_elements = [i for i in ELEMENTS.keys() if len(i) == 3]
	three_letter_list = []
	for i in three_letter_elements:
		i = i.lower()
		three_letter_list.append(i) if i in word.lower() else ''
	if three_letter_list:
		elements_are.append(three_letter_list)
	elements_are = [item for sublist in elements_are for item in sublist if item]
	return elements_are


a = elemental_forms('snack')
answer_a = [
	['Sulfur (S)', 'Nitrogen (N)', 'Actinium (Ac)', 'Potassium (K)'],
	['Sulfur (S)', 'Sodium (Na)', 'Carbon (C)', 'Potassium (K)'],
	['Tin (Sn)', 'Actinium (Ac)', 'Potassium (K)']
	]
print('Test case a:', a == answer_a)
# b = elemental_forms('beach')
# answer_b = [['Beryllium (Be)', 'Actinium (Ac)', 'Hydrogen (H)']]
# print('Test case b:', b == answer_b)
# c = elemental_forms('BEACH')
# answer_c = [['Beryllium (Be)', 'Actinium (Ac)', 'Hydrogen (H)']]
# print('Test case c:', c == answer_c)

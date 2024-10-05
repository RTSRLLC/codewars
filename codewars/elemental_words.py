from typing import List

from interview_questions import three

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
	elements_are = list()
	# check dict for single upper letter elements
	elements_are.append([f"{check_symbol(i)} ({i})" for i in list(word.upper()) if not f"{check_symbol(i)} ({i})".startswith('Invalid symbol')])
	# permutations for 2 letter elements
	list_word = list(word.upper())
	length = len(word)
	list_word_iter = iter(list_word)
	double_letter_perms = []
	for let in list_word:
		while length > 0:
			try:
				next_letter = next(list_word_iter)
				double_letter_perms.append(''.join(let + next_letter.lower()))
				length -= 1
			except StopIteration:
				list_word = list(word.upper())
				length = len(word)
				list_word_iter = iter(list_word)
		length = len(word)
		list_word = list(word.upper())
		list_word_iter = iter(list_word)
	elements_are.append(double_letter_perms)
	# permutations for 3 letter elements
	three_letter_elements = [i for i in ELEMENTS.keys() if len(i) == 3]
	three_letter_list = []
	for i in three_letter_elements:
		i = i.lower()
		three_letter_list.append(i) if i in word.lower() else ''
	if three_letter_list:
		elements_are.append(three_letter_list)
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

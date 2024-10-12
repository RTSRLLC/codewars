#
# ELEMENTS = {
# 	'H': 'Hydrogen', 'He': 'Helium', 'Li': 'Lithium', 'Be': 'Beryllium', 'B': 'Boron', 'C': 'Carbon', 'N': 'Nitrogen', 'O': 'Oxygen', 'F': 'Fluorine',
# 	'Ne': 'Neon', 'Na': 'Sodium', 'Mg': 'Magnesium', 'Al': 'Aluminium', 'Si': 'Silicon', 'P': 'Phosphorus', 'S': 'Sulfur', 'Cl': 'Chlorine', 'Ar': 'Argon',
# 	'K': 'Potassium', 'Ca': 'Calcium', 'Sc': 'Scandium', 'Ti': 'Titanium', 'V': 'Vanadium', 'Cr': 'Chromium', 'Mn': 'Manganese', 'Fe': 'Iron', 'Co': 'Cobalt',
# 	'Ni': 'Nickel', 'Cu': 'Copper', 'Zn': 'Zinc', 'Ga': 'Gallium', 'Ge': 'Germanium', 'As': 'Arsenic', 'Se': 'Selenium', 'Br': 'Bromine', 'Kr': 'Krypton',
# 	'Rb': 'Rubidium', 'Sr': 'Strontium', 'Y': 'Yttrium', 'Zr': 'Zirconium', 'Nb': 'Niobium', 'Mo': 'Molybdenum', 'Tc': 'Technetium', 'Ru': 'Ruthenium',
# 	'Rh': 'Rhodium', 'Pd': 'Palladium', 'Ag': 'Silver', 'Cd': 'Cadmium', 'In': 'Indium', 'Sn': 'Tin', 'Sb': 'Antimony', 'Te': 'Tellurium', 'I': 'Iodine',
# 	'Xe': 'Xenon', 'Cs': 'Caesium', 'Ba': 'Barium', 'La': 'Lanthanum', 'Ce': 'Cerium', 'Pr': 'Praseodymium', 'Nd': 'Neodymium', 'Pm': 'Promethium',
# 	'Sm': 'Samarium', 'Eu': 'Europium', 'Gd': 'Gadolinium', 'Tb': 'Terbium', 'Dy': 'Dysprosium', 'Ho': 'Holmium', 'Er': 'Erbium', 'Tm': 'Thulium',
# 	'Yb': 'Ytterbium', 'Lu': 'Lutetium', 'Hf': 'Hafnium', 'Ta': 'Tantalum', 'W': 'Tungsten', 'Re': 'Rhenium', 'Os': 'Osmium', 'Ir': 'Iridium',
# 	'Pt': 'Platinum',
# 	'Au': 'Gold', 'Hg': 'Mercury', 'Tl': 'Thallium', 'Pb': 'Lead', 'Bi': 'Bismuth', 'Po': 'Polonium', 'At': 'Astatine', 'Rn': 'Radon', 'Fr': 'Francium',
# 	'Ra': 'Radium', 'Ac': 'Actinium', 'Th': 'Thorium', 'Pa': 'Protactinium', 'U': 'Uranium', 'Np': 'Neptunium', 'Pu': 'Plutonium', 'Am': 'Americium',
# 	'Cm': 'Curium', 'Bk': 'Berkelium', 'Cf': 'Californium', 'Es': 'Einsteinium', 'Fm': 'Fermium', 'Md': 'Mendelevium', 'No': 'Nobelium', 'Lr': 'Lawrencium',
# 	'Rf': 'Rutherfordium', 'Db': 'Dubnium', 'Sg': 'Seaborgium', 'Bh': 'Bohrium', 'Hs': 'Hassium', 'Mt': 'Meitnerium', 'Ds': 'Darmstadtium',
# 	'Rg': 'Roentgenium',
# 	'Cn': 'Copernicium', 'Uut': 'Ununtrium', 'Fl': 'Flerovium', 'Uup': 'Ununpentium', 'Lv': 'Livermorium', 'Uus': 'Ununseptium', 'Uuo': 'Ununoctium'
# 	}
#
#
# def check_singles(the_word: str):
# 	add_list = list()
# 	add_list.append(
# 		[f"{check_symbol(i)} ({i})" for i in list(the_word.upper()) if not f"{check_symbol(i)} ({i})".startswith('Invalid symbol')]
# 		)
# 	return add_list[0]
#
#
# def check_doubles(elements: dict, the_word: str) -> list:
# 	def reset_doubles() -> None:
# 		global list_word, length, list_word_iter
# 		list_word = list(the_word.upper())
# 		length = len(the_word)
# 		list_word_iter = iter(list_word)
#
# 	global list_word, length, list_word_iter
# 	length = len(the_word)
# 	list_word = list(the_word.upper())
# 	list_word_iter = iter(list_word)
#
# 	add_list = []
# 	for let in list_word:
# 		while length:
# 			try:
# 				form_letter = ''.join(let + next(list_word_iter).lower())
# 				add_list.append(
# 					f"{check_symbol(form_letter)} ({form_letter})" if elements.get(form_letter, 'Invalid symbol') != 'Invalid symbol' else ''
# 					)
# 				length -= 1
# 			except StopIteration:
# 				reset_doubles()
# 		reset_doubles()
# 	return add_list
#
#
# def check_triples(elements: dict, the_word: str) -> list:
#
# 	add_list = []
# 	three_letter_elements = [i for i in elements.keys() if len(i) == 3]
# 	for i in three_letter_elements:
# 		i = i.lower()
# 		add_list.append(i) if i in the_word.lower() else ''
# 	if add_list:
# 		add_list.append(add_list)
# 	return add_list
#
#
# def check_symbol(symbol: str):
# 	return ELEMENTS.get(symbol, 'Invalid symbol')
#
#
# def elemental_forms(word: str) -> list:
# 	global list_word, length, list_word_iter, elements_are, ELEMENTS
# 	length = len(word)
# 	list_word = list(word.upper())
# 	list_word_iter = iter(list_word)
#
# 	elements_are = list()
# 	elements_are.append(check_singles(the_word=word))
# 	elements_are.append([i for i in check_doubles(elements=ELEMENTS, the_word=word) if i != ''])
# 	elements_are.append(check_triples(elements=ELEMENTS, the_word=word))
#
# 	elements_are = [item for sublist in elements_are for item in sublist if item]
# 	zip_elements = dict(
# 		zip(
# 			["".join(i for i in list(i)[-3:] if i not in ('(', ')')) for i in elements_are],
# 			elements_are
# 			)
# 		)
# 	eliminate_useless_elements = [t for t in list(zip_elements.keys()) if t.lower() in word.lower()]
#
#
# 	return eliminate_useless_elements
#
#
# length = None
# list_word = None
# list_word_iter = None
# elements_are = None
#
# a = elemental_forms('snack')



word = 'snack'
word__ = list(word)
length_word = len(word)

word_a_list_original = ['S', 'N', 'C', 'K', 'Sn', 'Na', 'Ac']
length_word_list = len(word_a_list_original)
word_d_list_lower = [i.lower() for i in word_a_list_original]

word_c_start = [i.lower() for i in word_d_list_lower if i.lower()[0] in word.lower()[0]]
index_1 = word_d_list_lower.index(word_c_start[0])
index_2 = word_d_list_lower.index(word_c_start[1])

word_d_list_lower.pop(index_1)
word_d_list_lower.pop(index_2 - 1)


word_e_possibilities = []
word_e_forming = ''

for i in word_c_start:
	_the_letter = word__.index(word_c_start[0])  # TODO needs resetting after some or all iterations
	word_e_forming += word__[_the_letter]
	enum_word_d_list = list(enumerate(word_d_list_lower, start=1))
	counter = 1
	for idx, j in enum_word_d_list:
		try:
			if j == word[idx]:
				word_e_forming += j
			else:
				continue
		except IndexError:
			continue





answer = [
	['Sulfur (S)', 'Nitrogen (N)', 'Actinium (Ac)', 'Potassium (K)'],
	['Sulfur (S)', 'Sodium (Na)', 'Carbon (C)', 'Potassium (K)'],
	['Tin (Sn)', 'Actinium (Ac)', 'Potassium (K)']
	]







# print(f"Test case a: {a == re_a=}")

# b = elemental_forms('beach')
# answer_b = [['Beryllium (Be)', 'Actinium (Ac)', 'Hydrogen (H)']]
# print('Test case b:', b == answer_b)
# c = elemental_forms('BEACH')
# answer_c = [['Beryllium (Be)', 'Actinium (Ac)', 'Hydrogen (H)']]
# print('Test case c:', c == answer_c)

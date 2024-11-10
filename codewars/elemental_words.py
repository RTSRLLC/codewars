from itertools import permutations
import time

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


def check_singles(the_word: str):
	return [f"{ELEMENTS.get(i, 'Invalid symbol')} ({i})" for i in list(the_word.upper()) if
			not f"{ELEMENTS.get(i, 'Invalid symbol')} ({i})".startswith('Invalid symbol')]


def check_doubles(elements: dict, the_word: str) -> list:
	def reset_doubles() -> None:
		nonlocal list_word, length, list_word_iter
		list_word = list(the_word.upper())
		length = len(the_word)
		list_word_iter = iter(list_word)

	length = len(the_word)
	list_word = list(the_word.upper())
	list_word_iter = iter(list_word)

	add_list = []
	for let in list_word:
		while length:
			try:
				form_letter = ''.join(let + next(list_word_iter).lower())
				add_list.append(
					f"{ELEMENTS.get(form_letter, 'Invalid symbol')} ({form_letter})" if elements.get(form_letter, 'Invalid symbol') != 'Invalid symbol' else ''
					)
				length -= 1
			except StopIteration:
				reset_doubles()
		reset_doubles()
	return add_list


def check_triples(elements: dict, the_word: str) -> list:
	add_list_test = [i.lower() for i in [i for i in elements.keys() if len(i) == 3] if i.lower() in the_word.lower()]
	return add_list_test if add_list_test else []


def elemental_forms(word: str) -> list:
	print(f"{word=}")
	if word == '':
		return []

	make_final_entry = lambda x: f"{ELEMENTS[x]} ({x})"

	elements_are = [
		check_singles(the_word=word), [i for i in check_doubles(elements=ELEMENTS, the_word=word) if i != ''], check_triples(elements=ELEMENTS, the_word=word)
		]

	final_elements = {
		i[i.lower().find(word.lower()):i.lower().find(word.lower()) + len(word)]
		for i in [
			i for i in
			[''.join(i) for i in permutations(
				[t for t in
				 list(
					 dict(
						 zip(
							 ["".join(i for i in list(i)[-3:] if i not in ('(', ')')) for i in
							  [item for sublist in elements_are for item in sublist if item]],
							 [item for sublist in elements_are for item in sublist if item]
							 )).keys())
				 if t.lower() in word.lower()], len(word))] if word.lower() in i.lower()
			] if word.lower() in i.lower()}

	out_list = []
	pre_out_list = []
	for i in final_elements:
		for idx, let in list(enumerate(i)):
			if i[idx].islower():
				continue
			try:
				if i[idx].isupper() and i[idx + 1].islower():
					pre_out_list.append(make_final_entry(let + i[idx + 1]))
				else:
					pre_out_list.append(make_final_entry(let))
			except IndexError:
				pre_out_list.append(make_final_entry(let))

		out_list.append(pre_out_list.copy())
		pre_out_list.clear()

	return out_list


a = elemental_forms('snack')
sorted_a = sorted(a)
answer = sorted(
	[
		['Sulfur (S)', 'Nitrogen (N)', 'Actinium (Ac)', 'Potassium (K)'],
		['Sulfur (S)', 'Sodium (Na)', 'Carbon (C)', 'Potassium (K)'],
		['Tin (Sn)', 'Actinium (Ac)', 'Potassium (K)']
		]
	)
print(f"Test case a: {answer == sorted_a=}")

b = elemental_forms('beach')
sorted_b = sorted(b)
answer_b = sorted([['Beryllium (Be)', 'Actinium (Ac)', 'Hydrogen (H)']])
print('Test case b:', answer_b == sorted_b)

c = elemental_forms('BEACH')
sorted_c = sorted(c)
answer_c = sorted([['Beryllium (Be)', 'Actinium (Ac)', 'Hydrogen (H)']])
print('Test case c:', sorted_c == answer_c)

d = elemental_forms('')

end_time = time.time()
print(f'Execution time: {(end_time - start_time) * 1000} milliseconds')

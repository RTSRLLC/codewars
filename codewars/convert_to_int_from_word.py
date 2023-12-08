def parse_int(string: str) -> int:
    """
    Takes in a string of words and returns the number that the string represents
    Args:
        string (): string of words

    Returns: int: number

    """
    split_string = string.split(" ")
    # remove unnecessary words
    for word in split_string[:]:  # Using slicing to create a copy of split_string
        if word not in words_to_ints.keys():
            split_string.remove(word)
    print(f"split string is: {split_string}")
    # quick check for single word
    if string in words_to_ints:
        return words_to_ints[string]

    # number = ["".join(word for word )]

    return


words_to_ints = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
    'hundred': 100,
    'thousand': 1000,
    'million': 1000000
}

a = parse_int('one')  # , 1)
b = parse_int('twenty')  # , 20)
c = parse_int('two hundred forty-six')  # , 246)
d = parse_int("seven hundred eighty-three thousand nine hundred and nineteen")  # , 783919)

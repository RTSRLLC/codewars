import itertools


def parse_int(string: str) -> int:
    """
    Takes in a string of words and returns the number that the string represents
    Args:
        string (): string of words

    Returns: int: number

    """

    def flatten_list(nested_list):
        result = []
        for element in nested_list:
            if isinstance(element, list):
                result.extend(flatten_list(element))
            else:
                result.append(element)
        return result

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

    # quick check for single word
    if string in words_to_ints:
        return words_to_ints[string]

    split_string = string.split(" ")  # split string into list of words

    # split words with hyphens
    for idx, word in enumerate(split_string):
        if '-' in word:
            split_string[idx] = word.split('-')
    split_string = flatten_list(split_string)  # flatten list

    # remove unnecessary words
    for word in split_string[:]:
        if word not in words_to_ints.keys():
            split_string.remove(word)

    # replace words with ints
    the_number = [
        words_to_ints[number]
        for number in split_string
        if number in words_to_ints
    ]
    # attach first number to output
    output = [the_number[0]]  # [7, 100, 80, 3, 1000, 9, 100, 19]
    for idx, num in enumerate(the_number[1:]):
        print(f"\n{'*' * 72}\nthe_number entering for loop: {the_number}\nand the num: {num}\n")
        print(f"current output: {output}\n")
        if idx < 10:
            if (idx + 1 % 100 == 0) or (idx + 1 % 1000 == 0):
                output.append(num * the_number[idx + 1])
                print(f"output is: {output}")
            if idx + 1 % 10 == 0:
                pass
        if num % 100 == 0 or num % 1000 == 0:
            pass

    return sum(output)


# a = parse_int('one')  # , 1)
# b = parse_int('twenty')  # , 20)
# c = parse_int('two hundred forty-six')  # , 246)
d = parse_int("seven hundred eighty-three thousand nine hundred and nineteen")  # , 783919)

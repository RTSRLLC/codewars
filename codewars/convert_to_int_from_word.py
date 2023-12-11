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

    for idx, word in enumerate(split_string):
        if '-' in word:
            split_string[idx] = word.split('-')

    split_string = flatten_list(split_string)  # flatten list

    # remove unnecessary words
    for word in split_string[:]:  # Using slicing to create a copy of split_string
        if word not in words_to_ints.keys():
            split_string.remove(word)

    the_number = [
        words_to_ints[number]
        for number in split_string
        if number in words_to_ints
    ]

    print(f"the_number: {the_number}")

    for idx, num in enumerate(the_number[:]):
        if num % 100 == 0:
            the_number.remove(num)
            print(f"the_number_2: {the_number}")
        elif num % 10 == 0:
            new_num = int(list(str(num))[0])
            the_number[idx] = new_num
            print(f"new_num: {the_number[idx]}")
            the_number.remove(num)
            print(f"the_number_3: {the_number}")
        elif num < 10:
            print(f"num: {num}")
            print(f"the_number_4: {the_number}")
            the_number.append(num)


    # result = []
    # for idx, num in enumerate(the_number[:]):
    #     print(f"the number is: {the_number}")
    #     print(f"result is: {result}")
    #     print(the_number[idx + 1] if idx + 1 < len(the_number) - 1 else None)
    #     print(f"if idx + 1 > len(the_number) - 1: {idx + 1 > len(the_number) - 1}")
    #     if idx + 1 > len(the_number) - 1:
    #         break
    #     # resolve for numbers less than 100
    #     print(f"the_number[idx + 2:]: {the_number[idx + 2:]}")
    #     print(f"any(the_number[idx + 2:]) > 100: {any(x > 100 for x in the_number[idx + 2:])}\n{'*' * 50}")
    #     if (100 <= the_number[idx + 1] < 1000) and (any(x > 100 for x in the_number[idx + 2:])):
    #         result.append(num * the_number[idx + 1])
    #         the_number.pop(idx + 1)
    #         result.append(sum(the_number[idx + 1:]))
    #
    #     elif (100 <= the_number[idx + 1] < 1000) and (all(x < 100 for x in the_number[idx + 2:])):
    #         result.append(num * the_number[idx + 1])
    #         the_number.pop(idx + 1)
    #         result.append(sum(the_number[idx + 1:]))
    #         break

    return


a = parse_int('one')  # , 1)
b = parse_int('twenty')  # , 20)
c = parse_int('two hundred forty-six')  # , 246)
print("*" * 50)
print("*" * 50)
print("*" * 50)
d = parse_int("seven hundred eighty-three thousand nine hundred and nineteen")  # , 783919)

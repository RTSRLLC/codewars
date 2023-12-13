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
    print(f"string is: {string}")

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

    print(f"the_number is: {the_number}")

    # attach first number to output
    output = int(the_number[0])
    tracking_idx = True
    for idx, num in enumerate(the_number[1:], start=1): # [90, 9, 1000, 9, 100, 90, 9]
        print(f"idx: {idx}, num: {num}")
        if not tracking_idx:
            tracking_idx = True
            continue
        if num % 100 == 0 or num % 1000 == 0:
            output *= num
            print(f"output is: {output}")
            if num == the_number[-1]:
                return output
        elif num % 10 == 0:
            output += num
            print(f"output is: {output}")
        elif num < 10:
            if num == the_number[-1]:
                if len(the_number[idx:]) > 1:
                    if the_number[idx - 1] % 100 == 0:
                        if the_number[idx + 1] % 100 == 0:
                            num *= the_number[idx + 1]
                            print(f"output is: {output}")
                            output += num
                            print(f"num is: {num}")
                            tracking_idx = False
                            continue
                    output += num
                    continue
                output += num
                return output
            if the_number[idx + 1] % 100 == 0:
                if the_number[idx - 1] % 100 == 0:
                    if the_number[idx + 1] % 100 == 0:
                        num *= the_number[idx + 1]
                        print(f"output is: {output}")
                        output += num
                        print(f"num is: {num}")
                        tracking_idx = False
                        continue
                output = (output + num) * the_number[idx + 1]
                tracking_idx = False
                print(f"output is: {output}")
        elif 11 < num < 20:
            output += num
            print(f"output is: {output}")

    return output


a = parse_int('one')  # , 1)
b = parse_int('twenty')  # , 20)
c = parse_int('two hundred forty-six')  # , 246)
d = parse_int("seven hundred eighty-three thousand nine hundred and nineteen")  # , 783919)
e = parse_int("one hundred")  # , 100)
f = parse_int("two thousand")  # , 2000)
g = parse_int("thirty-five thousand")  # , 35000)
h = parse_int("ninety-nine thousand nine hundred and ninety-nine")  # , 999999)
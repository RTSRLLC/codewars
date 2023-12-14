def parse_number_segment(segment: str, words_to_ints: dict) -> int:
    """
    Parse a segment of the number string into an integer.
    """
    segment_value = 0
    current = 0
    for word in segment.split():
        if word in words_to_ints:
            number = words_to_ints[word]
            if number == 100:
                current *= number
            else:
                current += number
        elif word == "hundred" and current == 0:
            current = 100
    segment_value += current
    return segment_value

def parse_int(string: str) -> int:
    words_to_ints = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
        'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12,
        'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
        'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40,
        'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90,
        'hundred': 100, 'thousand': 1000, 'million': 1000000
    }

    string = string.replace('-', ' ')
    string = string.replace(' and ', ' ')

    # Split string into pieces
    segments = []
    current_segment = []
    multiplier = 1
    total = 0
    for word in string.split()[::-1]:
        if word in ['thousand', 'million']:
            total += parse_number_segment(' '.join(current_segment[::-1]), words_to_ints) * multiplier
            current_segment = []
            multiplier = words_to_ints[word]
        else:
            current_segment.append(word)
    if current_segment:
        total += parse_number_segment(' '.join(current_segment[::-1]), words_to_ints) * multiplier

    return total



a = parse_int('one')  # , 1)
b = parse_int('twenty')  # , 20)
c = parse_int('two hundred forty-six')  # , 246)
d = parse_int("seven hundred eighty-three thousand nine hundred and nineteen")  # , 783919)
e = parse_int("one hundred")  # , 100)
f = parse_int("two thousand")  # , 2000)
g = parse_int("thirty-five thousand")  # , 35000)
h = parse_int("ninety-nine thousand nine hundred and ninety-nine")  # , 999999)
i = parse_int("two hundred three thousand")  # , 203000)
j = parse_int("five hundred thousand three hundred")  #, 500300)
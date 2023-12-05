def first_non_repeating_letter(s: str) -> str:
    """
    Return the first non-repeating character in a string.

    Args:
        s (str): The input string to be evaluated.

    Returns:
        str: The first non-repeating character in the input string, or an
        empty string if no such character exists.

    Example:
        >>> first_non_repeating_letter("stress")
        't'
        >>> first_non_repeating_letter("moonmen")
        'e'
        >>> first_non_repeating_letter("")
        ''
        >>> first_non_repeating_letter("abba")
        ''
    """
    char_count = {}
    for char in s:
        lower_char = char.lower()
        char_count[lower_char] = char_count.get(lower_char, 0) + 1

    return next((char for char in s if char_count[char.lower()] == 1), '')



a = first_non_repeating_letter('a')  # 'a')
b = first_non_repeating_letter('stress')  # , 't')
c = first_non_repeating_letter('moonmen')  # , 'e')
d = first_non_repeating_letter('')  # , '')
e = first_non_repeating_letter('abba')  # , '')
f = first_non_repeating_letter('aa')  # , '')
g = first_non_repeating_letter('~><#~><')  # , '#')
h = first_non_repeating_letter('hello world, eh?')  # , 'w')
i = first_non_repeating_letter('sTreSS')  # , 'T')
j = first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!')  # , ',')

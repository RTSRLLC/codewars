def order(sentence: str) -> str:
    """
    Reorders words in a sentence based on the digit found in each word.

    This function takes a sentence and reorders the words based on a single digit found in each word.
    Words are expected to contain exactly one digit. If a word does not contain a digit or if
    multiple digits are present in a single word, the behavior is not defined. If the sentence is
    empty, it returns an empty string.

    Args:
        sentence (str): The sentence to reorder. Words in the sentence are separated by spaces.

    Returns:
        str: A reordered sentence based on the digits found in each word.

    Example:
        >>> order("is2 Thi1s T4est 3a")
        'Thi1s is2 3a T4est'

    Note:
        - The function assumes that each word in the sentence contains exactly one digit.
        - Words are defined as sequences of characters separated by spaces.
        - The order of words in the output is determined by the numerical order of the digits in the words.
    """
    if sentence == "":
        return ""

    key = (i + 1 for i in range(len(sentence.split(" "))))
    val = (None for i in range(len(sentence.split(" "))))
    out = dict(zip(key, val))

    for wds in sentence.split(" "):
        for wd in wds:
            # find digit in lets
            if wd.isdigit():
                out[int(wd)] = wds

    return " ".join(out.values())


test = "is2 Thi1s T4est 3a"  # "Thi1s is2 3a T4est"
test1 = "4of Fo1r pe6ople g3ood th5e the2"  # "Fo1r the2 g3ood 4of th5e pe6ople"
test3 = ""  # ""

t = order(test)
t1 = order(test1)
t3 = order(test3)

def first_non_repeating_letter(s: str) -> str:
    """Return the first non-repeating character in a string"""
    if not s:
        return ''
    if len(s) == 1:
        return s
    out = ""
    ss = list(s)
    for i in ss:
        if i not in ss[ss.index(i) + 1:]:
            return i
        print(f'{i in ss[ss.index(i):]}')
        continue


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

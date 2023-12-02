def first_non_repeating_letter(s: str) -> str:
    """Return the first non-repeating character in a string"""
    if not s:
        return ''
    if len(s) == 1:
        return s
    ss = list(s)
    sss = ss.copy()
    for i in sss:
        if i not in sss[sss.index(i) + 1:]:
            return ss.pop(ss.index(i))
        print(f'{i in sss[sss.index(i):]}')
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

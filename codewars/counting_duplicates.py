def duplicate_count(text):
    text = list(text.lower())
    out_dict = {}
    for i in text:
        if text.count(i) > 1:
            out_dict[i] = text.count(i)
    return len(out_dict.values()) if len(out_dict.values()) > 0 else 0


a = duplicate_count("") # , 0)
b = duplicate_count("abcde") # , 0)
c = duplicate_count("abcdeaa") # , 1)
d = duplicate_count("abcdeaB") # , 2)
e = duplicate_count("Indivisibilities") # , 2)
f = duplicate_count("aA11") # , 2)
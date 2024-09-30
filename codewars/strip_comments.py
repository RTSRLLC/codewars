import string


def strip_comments(strng: str, markers: list) -> str:
    """
    Removes comments from a string. Comments are denoted by specific marker characters.
    
    Parameters:
    strng (str): The input string containing lines of text, potentially with comments.
    markers (list): A list of characters that denote the start of a comment.
    
    Returns:
    str: The input string with comments removed. Each line is stripped of any text following the comment markers.
    """
    out_string = ''
    out_list = []
    for i in strng.split('\n'):
        for j in i:
            if j in markers:
                break
            out_string += j
        out_list.append(out_string.rstrip())
        out_string = ''
    return '\n'.join(out_list)


# a = strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!'])
# print(f"{'-' * 72}\na is...")
# print('apples, pears\ngrapes\nbananas')
# aa = 'apples, pears\ngrapes\nbananas'
# print(a)
# print(a.strip() == aa.strip())
# print('*' * 30)
b = strip_comments('a #b\nc\nd $e f g', ['#', '$'])  # , 'a\nc\nd')
print(repr('a\nc\nd'))
print('*' * 30)
# c = strip_comments(' a #b\nc\nd $e f g', ['#', '$'])  # , ' a\nc\nd')
# print('c is...')
# print('a\nc\nd')
# print('*' * 30)

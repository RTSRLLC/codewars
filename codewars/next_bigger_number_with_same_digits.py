def next_bigger(n: int) -> int:
    """
    Finds the next bigger number that can be formed by rearranging the digits of the given number.

    Parameters:
    n (int): The input number whose digits are to be rearranged.

    Returns:
    int: The next bigger number formed by rearranging the digits. 
         Returns -1 if no such number exists.
    """
    digits = list(str(n))
    length = len(digits)
    
    # the rightmost digit that is smaller than the digit next to it
    for i in range(length - 2, -1, -1):
        if digits[i] < digits[i + 1]:
            break
    else:
        return -1
    
    # the smallest digit on the right side of the found digit that is larger than it
    for j in range(length - 1, i, -1):
        if digits[j] > digits[i]:
            break
    
    digits[i], digits[j] = digits[j], digits[i]
    
    return int(''.join(digits[:i + 1] + sorted(digits[i + 1:])))


a = next_bigger(21)  # ,   -1)
b = next_bigger(513)  # ,  531)
c = next_bigger(2017)  # , 2071)
d = next_bigger(414)  # ,  441)
e = next_bigger(144)  # ,  414)
f = next_bigger(1234567890)  # , 1234567908)

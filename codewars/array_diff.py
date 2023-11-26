def array_diff(a: list, b: list) -> list:
    """
    Returns a list that contains all the elements of 'a' that are not in 'b'.

    This function takes two lists, 'a' and 'b', and returns a new list containing
    all the elements from 'a' that are not present in 'b'. The order of the elements
    in the returned list is the same as in 'a'. If 'b' is empty, all elements from 'a'
    are returned.

    Args:
        a (list): The list to filter.
        b (list): The list containing elements to exclude from 'a'.

    Returns:
        list: A new list containing elements from 'a' that are not in 'b'.

    Examples:
        >>> array_diff([1, 2], [1])
        [2]
        >>> array_diff([1, 2, 2], [1])
        [2, 2]
        >>> array_diff([1, 2, 2], [2])
        [1]
        >>> array_diff([1, 2, 2], [])
        [1, 2, 2]
        >>> array_diff([1, 2, 3], [1, 2])
        [3]
    """
    return [x for x in a if x not in b]




a = array_diff([1,2], [1])      #, [2], "a was [1,2], b was [1], expected [2]")

b = array_diff([1,2,2], [1])    #, [2,2], "a was [1,2,2], b was [1], expected [2,2]")

c = array_diff([1,2,2], [2])    #, [1], "a was [1,2,2], b was [2], expected [1]")

d = array_diff([1,2,2], [])     # , [1,2,2], "a was [1,2,2], b was [], expected [1,2,2]")

f = array_diff([1,2,3], [1, 2]) # , [3], "a was [1,2,3], b was [1, 2], expected [3]")
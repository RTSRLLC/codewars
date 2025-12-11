def object_attributes(*, obj: object, kwords: list = None) -> list[str]:
    """
    Retrieve and process non-special attributes of an object, with optional keyword filtering.

    This function inspects the provided object using `dir()` to get all attributes, filters out
    special (dunder) methods, sorts the remaining names, and prints the count followed by each name.
    It stores the full list in a dictionary under 'all attributes'. If keywords are provided,
    it calls the nested `get_funcs()` to search for attributes containing those keywords (case-insensitive),
    prints matching groups, and adds them to the dictionary under 'keyword attributes'.

    Parameters:
    obj (object): The object to inspect for attributes.
    kwords (list, optional): A list of keywords to search for within attribute names. Defaults to None.

    Returns:
    dict: A dictionary containing 'all attributes' (sorted list of non-dunder attributes) and optionally
          'keyword attributes' (dict mapping keywords to lists of matching attributes).

    Notes:
    - The function has side effects: it prints the attribute count, each attribute name, and keyword matches if applicable.
    - Keyword matching is case-insensitive and checks for substring presence.
    - The return type annotation specifies list[str], but the actual return is a dict; this may be an inconsistency.
    - Useful for object introspection, debugging, or filtering methods/properties by keywords.
    """

    def get_funcs():
        """
        Search for attributes containing specified keywords and print/store the matches.

        This nested function is called if `kwords` is provided. It creates a dictionary mapping each keyword
        to a sub-dictionary with 'keywords' key holding a list of attributes from `lst` that contain the keyword
        (case-insensitive substring match). It prints each keyword and its matches if any exist, then updates
        the outer scope's `outgoing` dictionary with these results under 'keyword attributes'.

        Notes:
        - Relies on `lst`, `kwords`, and `outgoing` from the outer scope (nonlocal variables).
        - Only prints and stores if matches are found for a keyword.
        - No return value; modifies `outgoing` in place.
        """
        fun_calls = {}
        if kwords:
            for i in kwords:
                is_there = [j for j in lst if i.lower() in j]
                fun_calls[i] = {'keywords': is_there}
        for k, v in fun_calls.items():
            for kk, vv in v.items():
                if vv:
                    print(f"\n{k}\n{vv}")
        outgoing['keyword attributes'] = fun_calls

    outgoing = {}
    lst = sorted(
        name
        for name in dir(obj)
        if not (name.startswith("__") and name.endswith("__"))
    )
    print(f"length lst: {len(lst)}")
    for name in lst:
        print(name)

    outgoing['all attributes'] = lst

    get_funcs()

    return outgoing
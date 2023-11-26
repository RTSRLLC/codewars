def DNA_strand(dna: str) -> str:
    """
    Return the complementary DNA strand to the given DNA sequence.

    Each nucleotide in the DNA sequence is replaced with its complementary nucleotide:
    'A' is replaced with 'T', 'T' with 'A', 'C' with 'G', and 'G' with 'C'. This
    mimics the base-pairing rules in DNA where adenine (A) pairs with thymine (T)
    and cytosine (C) pairs with guanine (G).

    Args:
        dna (str): A string representing the DNA sequence.

    Returns:
        str: The complementary DNA sequence.

    Examples:
        >>> DNA_strand("ATTGC")
        "TAACG"
        >>> DNA_strand("GTAT")
        "CATA"
        >>> DNA_strand("AAGG")
        "TTCC"
        >>> DNA_strand("CGCG")
        "GCGC"
        >>> DNA_strand("ACGT")
        "TGCA"
    """
    return dna.translate(str.maketrans('ATCG','TAGC'))



a = DNA_strand("AAAA") #,"TTTT","String AAAA is")
b = DNA_strand("ATTGC") # ,"TAACG","String ATTGC is")
c = DNA_strand("GTAT") # ,"CATA","String GTAT is")
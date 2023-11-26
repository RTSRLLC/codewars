def rgb(r: int, g: int, b: int) -> str:
    """
    Convert RGB color values to a hexadecimal representation.

    Args:
        r (int): The red component (0 to 255).
        g (int): The green component (0 to 255).
        b (int): The blue component (0 to 255).

    Returns:
        str: The hexadecimal representation of the RGB color (e.g., 'FF0000' for pure red).
    """
    return ''.join([hex(x)[2:].upper().zfill(2) if 0 <= x <= 255 else '00' if x < 0 else 'FF' for x in [r, g, b]])


a = rgb(0, 0, 0) # 000000" # testing zero values")
b = rgb(1, 2, 3) # 010203" # testing near zero values")
c = rgb(255, 255, 255) # FFFFFF" # testing max values")
d = rgb(254, 253, 252) # FEFDFC" # testing near max values")
e = rgb(-20, 275, 125) # 00FF7D" # testing out of range values")
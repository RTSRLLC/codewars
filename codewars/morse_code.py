def decode_morse( morse_code: str ) -> str:
    """
    Decodes a string of Morse code into human-readable text.

    The function splits the Morse code string at spaces to separate individual Morse code characters
    and decodes each character using a predefined dictionary `MORSE_CODE`.
    Spaces in Morse code are represented by empty strings, which are converted to spaces in the output.
    Consecutive spaces in the decoded text are consolidated into single spaces.

    Args:
    morse_code (str): A string containing Morse code to be decoded.

    Returns:
    str: The decoded human-readable text from the provided Morse code.

    Examples:
    >>> decode_morse('.... . .-.. .-.. ---')
    'HELLO'
    >>> decode_morse('.- .-.. .. ...- .')
    'ALIVE'
    """
    return ("".join(
            [ MORSE_CODE[ i ] if i != "" else " " for i in morse_code.split( " " ) ] )
            .replace( "  ", " " ).strip())


def decode_bits( bits ):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    return bits.replace( '111', '-' ).replace( '000', ' ' ).replace( '1', '.' ).replace( '0', '' )


def decode_morse( morseCode ):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    return morseCode.replace( '.', MORSE_CODE[ '.' ] ).replace( '-', MORSE_CODE[ '-' ] ).replace( ' ', '' )


MORSE_CODE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I',
    '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0',
    '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(',
    '-.--.-': ')', '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
    '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS' }

# a = decode_morse( '.-' )  # , 'A')
# b = decode_morse( '--...' )  # , '7')
# c = decode_morse( '...-..-' )  # , '$')
# d = decode_morse( '.' )  # , 'E')
# e = decode_morse( '..' )  # , 'I')
# f = decode_morse( '. .' )  # , 'EE')
# g = decode_morse( '.   .' )  # , 'E E')
# h = decode_morse( '...-..- ...-..- ...-..-' )  # , '$$$')
# i = decode_morse( '----- .---- ..--- ---.. ----.' )  # , '01289')
# j = decode_morse( '.-... ---...   -..-. --...' )  # , '&: /7')
# k = decode_morse( '...---...' )  # , 'SOS')
# l = decode_morse( '... --- ...' )  # , 'SOS')
# m = decode_morse( '...   ---   ...' )  # , 'S O S')

"""
When transmitting the Morse code, the international standard specifies that:

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
"""

aa = decode_morse(decode_bits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')) #, 'HEY JUDE')

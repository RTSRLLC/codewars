def decode_morse(morse_code: str) -> str:
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
            [MORSE_CODE[i] if i != "" else " " for i in morse_code.split(" ")])
            .replace("  ", " ").strip())





MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}

a = decode_morse('.-') # , 'A')
b = decode_morse('--...') # , '7')
c = decode_morse('...-..-') # , '$')
d = decode_morse('.') # , 'E')
e = decode_morse('..') # , 'I')
f = decode_morse('. .') #, 'EE')
g = decode_morse('.   .') # , 'E E')
h = decode_morse('...-..- ...-..- ...-..-') # , '$$$')
i = decode_morse('----- .---- ..--- ---.. ----.') # , '01289')
j = decode_morse('.-... ---...   -..-. --...') # , '&: /7')
k = decode_morse('...---...') # , 'SOS')
l = decode_morse('... --- ...') # , 'SOS')
m = decode_morse('...   ---   ...') # , 'S O S')
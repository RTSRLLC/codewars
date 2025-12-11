# number upper lower

import string
import random




lets = list(string.ascii_letters)
punctuation = [
    '!', '@', '#', '$', '%', '^', '*', '(', ')',
    '-', '_', '+', '=', '[', ']', '{', '}', '|',
    ';', ':', "'", '"', ',', '.', '/', '?', '~', '`'
]
numbers = list(string.digits)

random.shuffle(lets)
random.shuffle(punctuation)
random.shuffle(numbers)

final = lets + punctuation + numbers
random.shuffle(final)

new_pass = ''
for i in range(17):
    char = random.choice(final)
    if len(new_pass) == 0:
        new_pass += char
        continue
    if char == new_pass[-1]:
        continue
    new_pass += char
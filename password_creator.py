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

def generate_password(digits: int):
    while True:
        new_pass = ''.join(random.choice(final) for _ in range(digits))
        if (any(i.isupper() for i in new_pass) and
            any(j.islower() for j in new_pass) and
            any(k in punctuation for k in new_pass) and
            any(z in numbers for z in new_pass)):
            return new_pass

pass_wrd = generate_password(27)
print(pass_wrd)
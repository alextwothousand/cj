import random
import string

specialChars = ['=', '+', '?', '-', '_', '^', '&']

def generateCode(length = 12):
    code = ''

    for i in range(0, (length - 2)):
        if random.randint(0, 1) == 0:
            code += random.choice(string.ascii_letters)
        else:
            code += f'{random.randint(0, 9)}'

    for i in range(0, 2):
        code += random.choice(specialChars)

    return code
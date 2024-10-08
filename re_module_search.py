

import re

char = input("Enter the  character: ")[0]

do = True

while do:
    if re.search("[A-Z]", char):
        print("It is a UpperCase Alphabet")
        break
    elif re.search("[a-z]", char):
        print("It  is a LowerCase Alphabet")
        break
    elif re.search("[0-9]", char):
        print("It is a Digit")
        break
    else:
        print("It is a special Character")
        break

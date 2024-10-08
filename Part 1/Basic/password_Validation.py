# Write a Python program to check the validity of a password (input from users).
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.
# Input
# W3r@100a
# Output
# Valid password

import re
password = str(input("Enter the password with min 6 and max 16 characters: "))


again = True
while again:
    if (len(password) < 6 or len(password) > 16):
        print("Password must be min 6 and max 16 characters")
        break
    elif not re.search("[A-Z]", password):
        print("A-Z missing")
        break
    elif not re.search("[a-z]", password):
        print("a-z missing")
        break
    elif not re.search("[0-9]", password):
        print("0-9 missing")
        break
    elif not re.search("[@#$]", password):
        print("@#$ missing")
        break
    else:
        print("Your Password is Valid")
        again = False
        break

'''
if again:
     print("Invalid  Password")

'''
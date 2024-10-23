# Write a Python program to create a Caesar encryption
# Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.
# For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.
# The method is named after Julius Caesar, who used it in his private correspondence.
# plaintext:  defend the east wall of the castle
# ciphertext: efgfoe uif fbtu xbmm pg uif dbtumf

plaintext = "defend the east wall of the castle"
plaintext_copy = "Defend The East Wall Of The Castle"


shift  = 1

def  caesarCipher(plaintext, shift):
    cipherText = ""
    for char in plaintext:
        if char.islower():
            shift_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            cipherText = cipherText + shift_char
        elif char.isupper():
            shift_char = chr(((ord(char) - ord('A') + shift) % 96) + ord('A'))
            cipherText = cipherText + shift_char
        else:
            cipherText = cipherText + chr(ord(char))
    return cipherText

print(caesarCipher(plaintext, shift))
print(caesarCipher(plaintext_copy, shift))
# Write a Python program to change a given string to a new string where the first and last chars have been exchanged

def change_char(word):
    return  word[-1].upper() + word[1:-1] + word[0].lower()

print(change_char("Hello world"))
print(change_char("Ajith"))
print(change_char("123445"))

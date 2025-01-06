# Write a Python program to remove the nth index character from a nonempty string

def remove_char(str, n):
    return str[:n] + str[n+1:]

print(remove_char("sahith", 2))
print(remove_char("Ajith",3))
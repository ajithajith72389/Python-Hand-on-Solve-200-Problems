# Write a Python program to count the number of characters (character frequency) in a string.
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

text = "google"

from collections import Counter

print(Counter(text))


#text = text.split(" ")

def freq_char(text):
    dict = {}
    for ele in text:
        keys = dict.keys()
        if ele in dict:
            dict[ele] += 1
        else:
            dict[ele] = 1
    return dict

print(freq_char(text))
print(freq_char("sahith kaja khan"))
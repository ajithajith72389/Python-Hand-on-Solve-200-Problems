# Write a Python program to count the number of characters (character frequency) in a string.
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

text = "Sahith Kaja Khan"

from collections import Counter

print(Counter(text))


#text = text.split(" ")

freq = {}

for chr in text:
    if chr in freq:
        freq[chr] += 1
    else:
        freq[chr] = 1
    
for chr, freq in freq.items():
    print(chr, freq, end=" ")
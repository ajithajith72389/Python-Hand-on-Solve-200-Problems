text = input()

text = text.split(" ")

freq = {}

for element in text:
    if element in freq:
        freq[element] += 1
    else:
        freq[element] = 1

for element, freq in freq.items():
    print(element, freq, end = " ")
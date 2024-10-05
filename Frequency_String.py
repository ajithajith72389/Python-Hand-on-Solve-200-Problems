# TCS NQT PROBLEM 2024 
text = input()

text = text.split(" ")

freq = {}

for element in text:
    if element in freq:
        freq[element] += 1
    else:
        freq[element] = 1

'''
# Sorted  by value

sorted_freq = dict(sorted(freq.items(), key = lambda item:item[0]))

#sorted by key

sorted_freq = dict(sorted(freq.items(), key = lambda item:item[1]))


'''

for element, freq in freq.items():
    print(element, freq, end = " ")
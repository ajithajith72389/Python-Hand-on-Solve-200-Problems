# Write a Python program to get the frequency of the elements in a list.
# input
# my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
# outout
# {10: 4, 20: 4, 40: 2, 50: 2, 30: 1}

my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]

freq = {}

for element  in my_list:
    if element in freq:
        freq[element] += 1
    else:
        freq [element] = 1

sorted_freq = dict(sorted(freq.items(), key = lambda item: item[1], reverse= True))

print(sorted_freq)


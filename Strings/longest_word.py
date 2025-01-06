# Write a Python function that takes a list of words and returns the length of the longest one 

def longest_word(name):
    words = name.split()
    temp = ""
    longest = 0
    for word in words:
        if longest < len(word):
            longest = len(word)
            temp = word
    return temp

name = "Sahith Kaja Khan"
print(longest_word(name))


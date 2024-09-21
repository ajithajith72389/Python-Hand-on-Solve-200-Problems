# Write a Python program that accepts a string and calculate the number of digits and letters
# Sample Data : "Python 3.2"
# Expected Output :
# Letters 6 
# Digits 2

sentence = input("Enter the sentence: ")
digit = 0
letter = 0
for  char in sentence:
    if char.isdigit():
        digit = digit + 1
    elif char.isalpha():
        letter = letter + 1

print("Digit: ", digit, " And letter : ", letter)  # This will print the number of digits and letters in the sentence. 

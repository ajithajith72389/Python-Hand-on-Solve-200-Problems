# Write a Python program to check whether an alphabet is a vowel or consonant

letter = input("Enter the letter you want: ")[0]

if  letter.lower() in 'a e i o u':
    print(letter, "is a vowel")
else:
    print(letter, "is a consonant")

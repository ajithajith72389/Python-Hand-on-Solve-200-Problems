n= int(input())
if n == 7:
    print(n,"We got it")
else:
    print(n,"Not the number we expected")
    

print("Next Program")
letter = input()
if letter == "a" or letter == "e" or letter == 'i' or letter == 'o' or letter == 'u':
    print(letter,"is vowel")
elif letter >= '0' and letter <= "9":
    print(letter,"is a Number")
else:
    print(letter,"is a consonant")
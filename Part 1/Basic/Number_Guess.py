# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

import random

guess = random.randint(1,9)

count = 1
again = True
while again:
    num = int(input("Enter the number you guess: "))
    if guess == num:
        print(f"You guessed  it!\nYou took {count} times")
        again = False
        
    elif guess >= num:
        print("The number is higher than you guess")
        count += 1
        #again = True
    elif guess <= num:
        print("The number is lower than you guess")
        count += 1
        #again = True
    
     

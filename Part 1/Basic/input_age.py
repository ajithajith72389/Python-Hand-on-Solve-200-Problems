# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("Enter your Name: ")
age = int(input("Enter your Age: "))

for i in range(age,  100):
    if age + i == 100:
        print(f"You will turn  100 years old in the year: {2024 + i} ") 

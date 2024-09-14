# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("Enter your Name: ")
age = int(input("Enter your Age: "))

year = (2024 - age) + 100
print(f"You will  be 100 years old in the year {year}")  # The \n is used to create

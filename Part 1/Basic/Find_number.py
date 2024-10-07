#  Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for  i in range(start, end+1):
    if i % 7 == 0 and i % 5 == 0:
        print(i, end= " ")

# Write a Python program to get the Fibonacci series between 0 to 50 

num = int(input())

a = 0
b = 1

for i in range(num):
    print(a, end=" ")
    c = a + b
    a, b = b, c
else:
    print("Program ended")
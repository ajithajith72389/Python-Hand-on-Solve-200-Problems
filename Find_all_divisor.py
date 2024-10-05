# TCS NQT PROBLEM
num = int(input())

total_sum = 0

for  i in range(1, num ):
    if num % i == 0:
        total_sum += i

if  num <= 1:
    print("False")
elif num  == total_sum:
    print("True")
else:
    print("False")



num = int(input("Enter the number: "))

if num < 0:
    for i in range(num, 1, 1):
        print(i, end = " ")
elif num > 0:
    for  i in range(num-1, -1, -1):
        print(i, end=" ")
else:
    print(num)

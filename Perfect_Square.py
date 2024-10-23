# python program to find out the perfect squares between the  given range

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for num in range(start, end):
    for i in range(1, num):
        if i * i == num:
            print(num, end = " ")
        elif i * i > num:
            break
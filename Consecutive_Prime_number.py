stop = int(input("Enter the  number of consecutive Prime Numbers: "))
start = int(input("Enter the starting number: "))

count = 0

for num in range(start, start+100):
    
    for i in range(2, num):
        if  (num % i) == 0:
            break
    else:
        count += 1
        if count < stop:
            print(num, end=", ")
        if count == stop:
            print(num)


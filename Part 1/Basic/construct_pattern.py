num = int(input("Enter the number: "))

for  i in range(1, num + 1):
    for j in range(i):
        print("* " ,end = "")
    print()
for i in range(num, 0, -1):
    for j in range(i):
        print("*  " ,end = "")
    print()    


# Add two numbers binary digit in OR Gate


def deci(num):
    lst = []
    while num:
        hexi = num % 2
        lst.append(hexi)
        num //= 2
    return lst

num1 = 5
num2 = 8

lst1 = deci(num1)
lst2 = deci(num2)

lst1.reverse()
lst2.reverse()
print(lst1)
print(lst2)

if len(lst1) < len(lst2):
    lst1, lst2 = lst2, lst1
    
while len(lst1) != len(lst2):
    lst2.append(0)
    
lst2.reverse()
print(lst2)

i = len(lst1) - 1
total = 0
for num in range(len(lst1)):
    if lst1[num] == 1 or lst2[num] == 1:
        total = total + pow(2, i)
    i = i - 1
    
print(total)


# use | this  operator for OR Gate 

print("Binary Addition: ", num1 | num2)
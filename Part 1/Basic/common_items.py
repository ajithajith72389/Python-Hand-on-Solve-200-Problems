# Write a Python program to find common items from two lists.
# input
# color1 = "Red", "Green", "Orange", "White"
# color2 = "Black", "Green", "White", "Pink"
# output
# {'Green', 'White'}

num1 = int(input("How many element you want in the first list: "))
num2 = int(input("How many element you want in the second list: "))

lst1 = []
lst2 = []
common = []
print("List 1:")
for i in range(num1):
    lst1.append(input())
    
print("List 2:")
for i in range(num2):
    lst2.append(input())
    
for i in range(num1):
    for j in range(num2):
        if  lst1[i] == lst2[j]:
            common.append(lst1[i])

print(common)


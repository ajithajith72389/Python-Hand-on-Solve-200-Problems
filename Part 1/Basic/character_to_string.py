# Convert a list of characters into a string
# Input ['a', 'b', 'c', 'd']
# Output abcd

num = int(input("Number of characters: "))

lst = []
for i in range(num):
    lst.append(input())
    
print("".join(lst))  # Output: abcd
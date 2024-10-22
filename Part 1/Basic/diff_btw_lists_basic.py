# Write a Python program to get the difference between the two lists
# Input 
# list1 = [1, 2, 3, 4]
# list2 = [1, 2]
# Output
# [3,4]

list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [1, 2, 3, 4, 5]
diff = []

if len(list1) <= len(list2):
    list1, list2 = list2, list1
    
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            break
    else:
        diff.append(list1[i])

print(diff)
# Write a Python program to check whether a list contains a sublist.
# Input
# a = [2,4,3,5,7]
# b = [4,3]
# c = [3,7]
# print(is_Sublist(a, b))
# print(is_Sublist(a, c))
# Output

def is_Sublist(l, s):
    subset = False
    if s == []:
        return True
    elif  s == l:
        return True
    elif  len(s) > len(l):
        return False
    else:
        for i in range(len(l)):
            if l[i] ==  s[0]:
                n = 1
                while n < len(s):
                    l[i+n] = s[n]
                    n = n + 1
                    subset = True
    return subset






a = [2,4,3,5,7]
b = [4,3]
c = [3,7]
print(is_Sublist(a, b))
print(is_Sublist(a, c))
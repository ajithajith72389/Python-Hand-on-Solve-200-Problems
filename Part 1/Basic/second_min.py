# Write a Python program to find the second smallest number in a list.
# input
# second_smallest([1, 2, -8, -2, 0])
# output
# -2

second_smallest = [1, 2, -8, -2, 0]

second_smallest = sorted(second_smallest)

print(second_smallest[1])
# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1 
# j = 0,1, n-1.
# Input
# Input number of rows: 3                                                                                       
# Input number of columns: 4  
# Output
# [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

no_rows = int(input("Enter number of rows: "))
no_cols = int(input("Enter number of cols: "))

multi_list = [[2 for col in range(no_cols)] for row in range(no_rows)]

for row in  range(no_rows):
    for col in range(no_cols):
        multi_list[row][col] = row * col

print(multi_list)

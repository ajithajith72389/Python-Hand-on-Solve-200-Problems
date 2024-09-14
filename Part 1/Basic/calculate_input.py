# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5 
# Expected Result : 615

num = int(input("Enter the number: "))
no_of_series = int(input("Enter your  choice of series: "))

series = 0
sum_res =0 
for i in range(0, no_of_series):
    series = series + (num * 10 **i )
    sum_res = sum_res + series
    
print(sum_res)
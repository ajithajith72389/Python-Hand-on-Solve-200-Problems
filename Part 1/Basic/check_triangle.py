# Write a Python program to check a triangle is valid or not

first = int(input("Enter the  first side of the triangle: "))
second = int(input("Enter  the second side of the triangle: "))
third = int(input("Enter  the third side of the triangle: "))

if  (first + second >= third) or (second + third >= first) or (third + first >= second):
    print("Yes, We can form a Tri-Angle..")
else:
    print("No,  We can't form a Tri-Angle..")  # Output: No, We can't form



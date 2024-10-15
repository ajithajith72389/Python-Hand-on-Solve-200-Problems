# Write a Python program to check a triangle is equilateral, isosceles or scalene.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.

side1 = int(input("Enter the first side of the triangle:"))
side2 = int(input("Enter the second side of the triangle:"))
side3 = int(input("Enter the third side of the triangel: "))

if side1 == side2 == side3:
    print("Equilateral Triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
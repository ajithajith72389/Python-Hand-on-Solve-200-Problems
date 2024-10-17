num1, num2, num3 = map(int, input("Enter the inputs: ").split())

num1_digit = set(str(num1))
num2_digit = set(str(num2))
num3_digit = set(str(num3))

common_digits = num1_digit.intersection(num2_digit).intersection(num3_digit)

if common_digits:
    print("".join(common_digits))
else:
    # print as -1
    print("-1")
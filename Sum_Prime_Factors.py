num = int(input("Enter the number: "))

copy = num

factors_sum = 0

while copy % 2 == 0:
    factors_sum += 2
    copy //= 2
    
i = 3

while i * i <= copy:
    while  copy % i == 0:
        factors_sum += i
        copy //= i
    i += 2

if copy > 2:
    factors_sum += copy

#fact_sum = sum(factors)
print(factors_sum)


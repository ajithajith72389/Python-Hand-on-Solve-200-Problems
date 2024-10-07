num = int(input("Enter a number you want: "))

# create a list for store each prime factor 

factors = []

while num % 2 == 0:
    factors.append(2)
    num = num // 2

# we already find  one prime factor, now we need to find the rest of them

i = 3
while i* i <= num:
    factors.append(i)
    num = num // i

#  if the remaining number is a prime number greater than 2

if  num > 2:
    factors.append(num)

#  print the prime factors of the number
print("Sum of prime factor: ",sum(factors))



     
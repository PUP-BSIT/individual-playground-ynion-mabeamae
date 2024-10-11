#num = int(input("Enter a 2-digit number: "))

#digit1 = num // 10
#digit2 = num % 10

#sum_of_digits = digit1 + digit2

#print("The sum of the digits is: ", sum_of_digits)

num = int(input("Enter a 2-digit number: "))

sum = 0

for digit in str(num):
    sum = sum + int(digit)

print("Sum of digits", sum)
print("Enter a number between 2 and 9 to be the base")
base = int(input())
maximum_value = base ** 4 - 1
print("Enter a base 10 number smaller than", maximum_value, " for conversion")
numerator = int(input())
while(quotient > 0):
    quotient = numerator / base
    remainder = numerator % base
    numerator = quotient
    print(quotient)
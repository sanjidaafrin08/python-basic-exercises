#Write a program that inputs two numbers and prints their sum, difference, product, and quotient.
a= int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
sum_result = a + b
difference = a - b
product = a * b
if b != 0:
    quotient = a / b
else:
    quotient = "Undefined"


print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)



#Swap two numbers without a third variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = a + b
b = a - b
a = a - b

print("After swapping: a =", a, "b =", b)

#Write a program that takes two numbers and checks if they are equal, not equal, greater than, less than, greater than or equal to, and less than or equal.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


if num1 == num2:
    print(num1, "is equal to", num2)
else:
    print(num1, "is not equal to", num2)


if num1 > num2:
    print(num1, "is greater than", num2)
else:
    print(num1, "is not greater than", num2)

if num1 < num2:
    print(num1, "is less than", num2)
else:
    print(num1, "is not less than", num2)


if num1 >= num2:
    print(num1, "is greater than or equal to", num2)
else:
    print(num1, "is not greater than or equal to", num2)


if num1 <= num2:
    print(num1, "is less than or equal to", num2)
else:
    print(num1, "is not less than or equal to", num2)

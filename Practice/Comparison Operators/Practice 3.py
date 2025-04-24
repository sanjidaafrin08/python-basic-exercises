#Develop a program that takes three numbers as input and prints the largest and smallest of the three numbers.
Number1 = float(input("Enter first number: "))
Number2 = float(input("Enter second number: "))
Number3 = float(input("Enter third number: "))
if Number1 >= Number2 and Number1 >= Number3:
    largest = Number1
elif Number2 >= Number1 and Number2 >= Number3:
    largest = Number2
else:
    largest = Number3
if Number1 <= Number2 and Number1 <= Number3:
    smallest = Number1
elif Number2 <= Number1 and Number2 <= Number3:
    smallest = Number2
else:
    smallest = Number3
print(largest, "is the largest")
print(smallest, "is the smallest")



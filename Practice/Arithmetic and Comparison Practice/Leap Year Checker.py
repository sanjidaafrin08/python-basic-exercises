# Leap Year Checker: Create a program that checks if a given year is a leap year or not.
x = int(input("Enter a year: "))

if (x % 400 == 0) or (x % 4 == 0 and x % 100 != 0):
    print(x, "is a Leap year")
else:
    print(x, "is Not a Leap year")
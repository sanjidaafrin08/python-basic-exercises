#Triangle Type Checker: Develop a program that takes three side lengths and determines if they form a valid triangle. Additionally, check if the triangle is acute, obtuse, or right-angled.
a = float(input("Enter the first side length: "))
b = float(input("Enter the second side length: "))
c = float(input("Enter the third side length: "))
if a + b > c and a + c > b and b + c > a:
    print("The lengths can form a valid triangle.")
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("The triangle is a right-angled triangle.")
    elif a**2 + b**2 > c**2 and a**2 + c**2 > b**2 and b**2 + c**2 > a**2:
        print("The triangle is an acute triangle.")
    else:
        print("The triangle is an obtuse triangle.")
else:
    print("The lengths cannot form a valid triangle.")
#Create a program that takes three side lengths and determines if they can form a triangle. Additionally, check if the triangle is equilateral, isosceles, or scalene.
a = float(input("Enter the first length: "))
b = float(input("Enter the second length: "))
c = float(input("Enter the third length: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    print("The lengths can form a triangle.")

    if a == b == c:
        print("The triangle is equilateral.")
    elif a == b or a == c or b == c:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")
else:
    print("The lengths cannot form a triangle.")

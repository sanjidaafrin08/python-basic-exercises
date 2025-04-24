#Temperature Converter and Comparator: Write a program that converts temperatures between Celsius and Fahrenheit and compares if two temperatures are the same in different units.
x = float(input("Enter temperature in Celsius: "))
y = float(input("Enter temperature in Fahrenheit: "))
converted_fahrenheit = (x * 9/5) + 32
if y== converted_fahrenheit:
    print("The temperatures are the same in Fahrenheit and Celsius.")
else:
    print("The temperatures are different in both units.")
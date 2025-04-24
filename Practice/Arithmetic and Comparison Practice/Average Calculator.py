# Average Calculator: Write a program that takes three numbers as input and calculates their average. Then, check if the average is greater than a specified threshold.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
average = (num1 + num2 + num3) / 3
threshold = float(input("Enter the threshold value: "))
if average > threshold:
    print("The average is greater than the threshold.")
else:
    print("The average is not greater than the threshold.")
print("The average of the three numbers is:", average)
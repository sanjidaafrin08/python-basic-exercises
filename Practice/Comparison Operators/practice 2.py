#Create a program that checks if a given number is positive, negative, or zero.

Number=float(input("Enter a number"))
if(Number==0):
    print("The number is 0")
elif(Number>0):
    print("The number is positive")
else:
    print("The number is negative")
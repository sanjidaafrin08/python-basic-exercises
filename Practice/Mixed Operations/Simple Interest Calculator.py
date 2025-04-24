#Write a program that calculates the simple interest given the principal, rate of interest, and time. Then, check if the interest is above a certain amount.
x = float(input("Enter a principal: "))
y = float(input("Enter rate of interest: "))
z = float(input("Enter time: "))

interest = (x * y * z) / 100
certain_amount = 1000

if interest > certain_amount:
    print("The interest is above a certain amount.")
else:
    print("The simple interest is: ",interest)

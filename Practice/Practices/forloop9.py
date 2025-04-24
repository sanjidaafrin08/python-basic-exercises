# Python program to check if a given number is an Armstrong number
number = int(input("Enter a number: "))
num_str = str(number)
num_digits = len(num_str)
sum_of_powers = 0
for digit in num_str:
    sum_of_powers += int(digit) ** num_digits
if sum_of_powers == number:
    print(number, "is an Armstrong number.")
else:
    print(number, "is NOT an Armstrong number.")

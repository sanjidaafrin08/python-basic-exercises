#Armstrong
num = 153
digits = str(num)
power = len(digits)

total = 0
for digit in digits:
    total += int(digit) ** power

if total == num:
    print("Armstrong Number")
else:
    print("Not Armstrong")

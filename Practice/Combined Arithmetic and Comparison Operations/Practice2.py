# Develop a program that simulates a simple banking system. Take an initial balance and a series of transactions (deposits and withdrawals), then print the final balance. Ensure that withdrawals do not exceed the current balance.

a = float(input("Enter the current balance: "))
b = float(input("Enter the deposit balance: "))
c = float(input("Enter the withdraw balance: "))

current_balance = a

if b > 0:
    current_balance =  current_balance+b

if c > 0:
    if c <= current_balance:
        current_balance = current_balance- c
    else:
        print("Insufficient balance for this withdrawal.")

print("The current balance is:", current_balance)
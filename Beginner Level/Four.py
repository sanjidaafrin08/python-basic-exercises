#Check if a number is a palindrome
num = int(input("Enter a number: "))
if str(num) == str(num)[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

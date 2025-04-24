#Python program to check if the given string is a palindrome.
given_string = input(str("Enter the string :"))
reverse_string = ""
for i in given_string:
    reverse_string = i + reverse_string
if (given_string == reverse_string):
    print("The string", given_string, "is a Palindrome.")
else:
    print("The string", given_string, "is NOT a Palindrome.")

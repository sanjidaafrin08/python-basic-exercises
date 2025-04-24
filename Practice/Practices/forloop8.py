#Python program that accepts a word from the user and reverses it.
given_string = input(str("Enter the string :"))
reverse_string = ""
for i in given_string:
    reverse_string = i + reverse_string
print(reverse_string)
#Email Validator
email = input("enter an email:")
if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")

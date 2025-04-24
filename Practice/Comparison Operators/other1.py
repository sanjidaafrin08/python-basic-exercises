#If total purchase amount more than 1000,customer will get free bag
expected_purchase_amount = 1000

customer_purchase_amount = int(input("Enter Amount: "))

if customer_purchase_amount > expected_purchase_amount:
    print("Congratulations! You get a free bag")
else:
    print("Thank you for your purchase.")
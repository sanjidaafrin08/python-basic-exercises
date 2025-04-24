#second largest
string = input("Enter numbers separated by spaces: ")

numbers = []
for n in string.split():
    numbers.append(int(n))


largest = max(numbers)
numbers.remove(largest)


second_largest = max(numbers)

print("The second largest number is:", second_largest)
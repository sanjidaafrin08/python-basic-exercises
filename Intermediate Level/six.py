# Problem 2: Largest number in array


string = input("Enter numbers separated by spaces: ")


numbers = []
for n in string.split():
    numbers.append(int(n))


largest = max(numbers)


print("The largest number is:", largest)
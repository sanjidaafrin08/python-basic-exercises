#Count frequency of each element
numbers = [1, 2, 2, 3, 3, 3, 4]
frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Frequencies:", frequency)

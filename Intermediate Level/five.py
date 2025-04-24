#Check if two strings are anagrams
def is_anagram(a, b):
    return sorted(a) == sorted(b)

a = input("Enter first string: ")
b = input("Enter second string: ")

print(is_anagram(a, b))

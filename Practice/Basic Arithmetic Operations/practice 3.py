#Develop a program that converts a given number of minutes into hours and minutes. For example, 125 minutes should be converted to 2 hours and 5 minutes.

number = int(input("Give a number: "))
x = number / 60
y = number % 60
print(number," minutes should be converted to " ,x ," hours and " ,y, " minutes.")



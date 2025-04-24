#Python program to calculate the sum of all the odd numbers within the given range.
# if the given range is 10
givenrange=10
sum=0
for i in range(1,givenrange):
    if(i%2!=0):
        sum+=i
print(sum )
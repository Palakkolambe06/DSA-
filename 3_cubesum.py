# Write a program for cube sum of n natural numbers.
n = int(input("Enter a number: "))
sum = 0
for i in range(1,n+1):
    sum += i**3
print(sum)

# By using formula - 
sum = 0
n = int(input("Enter a number: "))
sum = (n*(n+1)//2)**2
print(sum)
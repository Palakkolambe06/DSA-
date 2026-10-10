'''
A palindrome number is a number that reads the same forward and backward.
Examples
121 → forward: 121 → backward: 121 ✅
So, 121 is a palindrome.
1221 → forward: 1221 → backward: 1221 ✅
123 → forward: 123 → backward: 321 ❌
So, 123 is NOT a palindrome.

Program-1
num = 125
sum = 0
while num > 0:
    sum+= num % 10
    num = num // 10
print(sum)

Program-2
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    sum+= num % 10
    num = num // 10
print(sum)
'''
# Program-3
num = int(input("Enter a number: "))
sum = 0
n=num
while num > 0:
    sum=sum*10 + (num % 10)
    num = num // 10
if n==sum:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")



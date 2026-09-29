'''
An Armstrong number is a number where the sum of each digit raised to the power of the number of digits is equal to the original number.
Example: 153
153 has 3 digits, so raise each digit to power 3:
$$ 1^3 + 5^3 + 3^3 $$ $$ 1 + 125 + 27 = 153 $$
Since the result is 153, it is an Armstrong number. ✅
More examples
0 → Armstrong
1 → Armstrong
153 → Armstrong
370 → Armstrong
371 → Armstrong
407 → Armstrong
1634 → Armstrong
'''
# Program -1 
num = int(input("Enter a number: "))
len = len(str(num))
sum = 0 
n = num
while num > 0:
    sum += (num % 10) ** len
    num = num // 10
if n == sum:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")
'''# 1. Calculate Array Sum: Write a program to accept N integers into an array and calculate and display the sum of all the elements. 
n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

total = 0

for num in arr:
    total = total + num
print("Sum =", total)

#2. Find the smallest and Largest Element: Write a program to accept N integers into an array and find and display the largest element, second largest element, smallest element, second smallest element present in the array. 
n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

if n < 2:
    print("Enter at least two elements to find the second largest and second smallest.")
else:
    arr.sort()
    print("Largest =", arr[-1]) 
    print("Second largest =", arr[-2])
    print("Smallest =", arr[0])
    print("Second smallest =", arr[1])
    

# 3. Count Even and Odd Numbers: Write a program to accept N integers into an array and count and display the number of even and odd elements present in the array. 
n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
even_count = 0
odd_count = 0

for num in arr:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers =", even_count)
print("Odd numbers =", odd_count)
'''

# 4. Search an Element: Write a program to accept N integers into an array and search for a given number. Display an appropriate message indicating whether the number is present in the array or not and also display its position. 
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

target = int(input("Enter number to search: "))
position = -1

for i in range(n):
    if arr[i] == target:
        position = i + 1
        break

if position != -1:
    print(target, "is present at position", position)
else:
    print(target, "is not present in the array")


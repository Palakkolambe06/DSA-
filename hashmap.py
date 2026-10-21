# Write a program to count frequency 
arr = [1, 2, 2, 3, 3, 3, 4]

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)



'''

arr = [1, 2, 3, 4 , 1, 2, 3, 4]

freq = {}
for num in arr:
    if num is freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)


def countfreq(n):
    freq = [0] * 10

    while(n!=0):
        last digit = n % 10
        freq[last_digit] += 1
        n // 10

    return freq

n = 12344467974
res = countfreq(n)
for i in range(len(res)):
    print(f"(i) -->{res[i]}")
'''


def countfreq(n):
    freq = [0] * 10

    while n != 0:
        last_digit = n % 10
        freq[last_digit] += 1
        n = n // 10

    return freq

n = 12344467974
res = countfreq(n)

for i in range(len(res)):
    print(f"{i} --> {res[i]}")


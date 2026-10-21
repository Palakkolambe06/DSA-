
def countfreq(n, k):
    freq = [0] * 10

    while n != 0:
        last_digit = n % 10
        freq[last_digit] += 1
        n = n // 10

    return freq[k]


n = 1213521333315
k = 3

res = countfreq(n, k)
print(res)

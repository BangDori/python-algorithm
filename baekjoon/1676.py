N = int(input())

count_125 = N // 125
count_25 = N // 25 - count_125
count_5 = N // 5 - (count_125 + count_25)

print((count_125 * 3) + (count_25 * 2) + count_5)
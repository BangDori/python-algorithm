N = int(input())

exp = 1
while N > exp * 2:
    exp *= 2

if N == 1:
    print(1)
else:
    print((N - exp) * 2)
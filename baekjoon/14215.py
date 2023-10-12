side = list(map(int, input().split()))

side.sort(reverse=True)
a, b, c = side

if (b+c) <= a:
    print((b+c-1) + b + c)
else:
    print(a+b+c)

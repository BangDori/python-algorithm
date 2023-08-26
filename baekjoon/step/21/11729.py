def hanoi(n, start, mid, to):
    if n == 1:
        print("%d %d" % (start, to))
        return

    hanoi(n-1, start, to, mid)
    print("%d %d" % (start, to))
    hanoi(n-1, mid, start, to)

n = int(input())
print(pow(2, n)-1)
hanoi(n, 1, 2, 3)
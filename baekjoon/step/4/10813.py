# 바구니의 크기(n), 반복 횟수(m)
n, m = map(int, input().split())
basket = [i for i in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    temp = basket[x]
    basket[x] = basket[y]
    basket[y] = temp

for i in range(1, n+1):
    print(basket[i], end=' ')
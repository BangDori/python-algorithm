# 바구니의 개수(n), 공을 넣는 반복 수(m)
n, m = map(int, input().split())
basket = [0 for _ in range(n)] # 바구니

for _ in range(m):
    start, end, ball = map(int, input().split())
    
    for i in range(start-1, end):
        basket[i] = ball

for i in range(n):
    print(basket[i], end=' ')
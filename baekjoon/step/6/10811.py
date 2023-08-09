# 바구니의 크기(n), 역순으로 반복할 횟수(m)
n, m = map(int, input().split())
basket = [i for i in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    # basket[start:end+1] = basket[start:end+1][::-1]

    for i in range(end-start):
        if end-i < start+i:
            break
        
        temp = basket[end-i]
        basket[end-i] = basket[start+i]
        basket[start+i] = temp
    
for i in range(1, n+1):
    print(basket[i], end=' ')
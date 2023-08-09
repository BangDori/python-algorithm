# 10 5
# 1 10 4 9 2 3 8 5 7 6
n, x = map(int, input().split()) # 수열의 크기(n)와 x보다 작은 수
array = list(map(int, input().split()))

for i in range(len(array)):
    if array[i] < x:
        print(array[i], end=' ')
tot_chess = [1, 1, 2, 2, 2, 8]
cur_chess = list(map(int, input().split()))

for i in range(len(tot_chess)):
    print(tot_chess[i] - cur_chess[i], end=' ')
"""
    1 sec, 256 MB

    N * N개의 수가 N * N 크기의 표

    (x1, y1) ~ (x2, y2) 까지의 합을 구하는 프로그램

    3 * 3
    => [0, 1, 2, 3, 4, 5, 6, 7, 8]
    0, 1
"""

import sys
input = sys.stdin.readline

# 표의 크기, 합을 구해야 하는 횟수
table_size, sum_count = map(int, input().split())

table = [0]
table_sum = [0]
for _ in range(table_size):
    table += list(map(int, input().split()))

table_sum = []
for idx, num in enumerate(table):
    if idx == 0:
        table_sum.append(num)
        continue
    table_sum.append(table_sum[idx-1] + num)

for _ in range(sum_count):
    x1, y1, x2, y2 = map(int, input().split())

    x1 -= 1
    x2 -= 1

    answer = 0
    for x in range(x1, x2+1):
        if x * table_size + y1 == x * table_size + y2:
            answer += table[x * table_size + y2]
        elif (x * table_size + y1) % table_size == 0:
            answer = table_sum[x * table_size + y2]
        else:
            answer += table_sum[x * table_size + y2] - table_sum[x * table_size + y1 - 1]

    print(answer)
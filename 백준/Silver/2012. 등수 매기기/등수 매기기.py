import sys
input = sys.stdin.readline

N = int(input())
expect_ranks = [int(input()) for _ in range(N)]

expect_ranks.sort()

rank = 1
answer = 0
for expect in expect_ranks:
    answer += abs(rank - expect)
    rank += 1

print(answer)
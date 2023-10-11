import sys
input = sys.stdin.readline

racer_count, pass_count = map(int, input().split())
racer_rank = [0 for _ in range(racer_count)]
first_contest = []

for rid in range(1, racer_count+1):
    rank = int(input())

    first_contest.insert(rank-1, rid)

second_contest = first_contest[0:pass_count]
second_contest.reverse()

result = []

for rid in second_contest:
    rank = int(input())

    result.insert(rank-1, rid)

for winner in result[0:3]:
    print(winner)

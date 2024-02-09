import sys
input = sys.stdin.readline

n = int(input())
votes = int(input())
candidate = list(map(int, input().split()))

result = []
vote_cnt = []

for person in candidate:
    if person in result: vote_cnt[result.index(person)] += 1
    else:
        if len(result) >= n:
            min_idx = vote_cnt.index(min(vote_cnt))
            del result[min_idx]
            del vote_cnt[min_idx]
        result.append(person)
        vote_cnt.append(1)

result.sort()
print(*result)
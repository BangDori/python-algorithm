import sys
input = sys.stdin.readline

people = int(input())
times = list(map(int, input().split()))
times.sort()

acc = []
for idx in range(len(times)):
    if idx == 0:
        acc.append(times[idx])
        continue
    acc.append(times[idx] + acc[idx-1])

answer = 0
for idx in range(len(times)):
    answer += acc[idx]
print(answer)
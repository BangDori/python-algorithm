from heapq import heapify, heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
voteCount = [int(input()) * -1 for _ in range(N)]
answer = 0

if N > 1:
    candidate = abs(voteCount.pop(0))
    heapify(voteCount)

    while candidate <= abs(voteCount[0]):
        heappush(voteCount, heappop(voteCount) + 1)
        answer += 1
        candidate += 1

print(answer)
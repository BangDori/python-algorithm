from bisect import bisect_right
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = []
for i in range(N):
    current_ink = A[i]
    answer.append(bisect_right(B, current_ink) - (i+1))
print(*answer)
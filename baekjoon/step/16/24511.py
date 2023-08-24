from collections import deque

queue = deque()

# 자료구조의 개수
N = int(input())
# i번 자료구조 0 = 큐, 1 = 스택
A = list(map(int, input().split()))
# i번 자료구조에 들어 있는 원소
B = list(input().split())
# 삽입할 수열의 길이
M = int(input())
# M의 수열 C
C = list(input().split())

for i in range(N):
    if A[i] == 0:
        queue.append(B[i])

if len(queue) == 0:
    print(" ".join(C))
else:
    for i in range(M):
        queue.appendleft(C[i])
        print(queue.pop(), end=' ')
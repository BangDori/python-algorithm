from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque([i+1 for i in range(N)])
answer = []

while queue:
    queue.rotate(-K)
    answer.append(str(queue.pop()))

print("<{0}>".format(", ".join(answer)))
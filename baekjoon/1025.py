from collections import deque
import sys
input = sys.stdin.readline

size = int(input())
seq = list(map(int, input().split()))
seq.sort()

if size == 1 or size == 2:
    print(size)
else:
    answer = 2

    pointer = 0
    queue = deque([])
    while pointer < len(seq):
        if len(queue) < 2:
            queue.append(seq[pointer])
            pointer += 1
            continue
        
        if queue[0] + queue[1] > seq[pointer]:
            # right 이동
            queue.append(seq[pointer])
            pointer += 1
        else:
            # left 이동
            if answer < len(queue):
                answer = len(queue)
            queue.popleft()
    
    if answer < len(queue):
        answer = len(queue)    
    print(answer)
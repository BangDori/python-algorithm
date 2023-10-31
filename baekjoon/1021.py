from collections import deque
import sys
input = sys.stdin.readline

queue_size, count = map(int, input().split())
find_list = list(map(int, input().split()))

circle_queue = deque([i for i in range(1,queue_size+1)])
answer = 0

for i in range(count):
    left = 0
    right = len(circle_queue)-1
    while left <= right:
        if circle_queue[left] == find_list[i] or circle_queue[right] == find_list[i]:
            break

        left += 1
        right -= 1

    if circle_queue[left] == find_list[i]:
        answer += left
        circle_queue.rotate(-left)
    else:
        answer += len(circle_queue)-right
        circle_queue.rotate(len(circle_queue)-right)
    circle_queue.popleft()
    
print(answer)

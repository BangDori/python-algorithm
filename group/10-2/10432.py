from collections import deque
import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    island = list(map(int, input().split()))
    test_id = island.pop(0)
    queue = deque([(0, 12)])
    answer = -1

    while queue:
        left, right = queue.popleft()
        answer += 1

        min_is = min(island[left:right])
        pos = -1
        for i in range(left, right+1):
            if i >= 12:
                break
            island[i] -= min_is

            if pos == -1 and island[i] > 0:
                pos = i
            
            if pos != -1 and island[i] <= 0:
                queue.append((pos, i))
                pos = -1
        
    print(test_id, answer)
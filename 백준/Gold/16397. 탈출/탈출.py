from collections import deque
import sys
input = sys.stdin.readline

MAX_LED = 99999

# 2
def is_enable_click_B(N):
    if N * 2 <= 99_999:
        return True
    return False

def clickedB(N):
    if N == 0:
        return 0
    
    result = N * 2
    for i in range(1, 6):
        if result < pow(10, i):
            result -= pow(10, i-1)
            break

    return result

old_LED, click_count, new_LED = map(int, input().split())

queue = deque([(old_LED, 0)])
visited = [float('inf') for _ in range(100000)]
visited[old_LED] = 0

answer = 'ANG'
while queue:
    current_LED, current_click_count = queue.popleft()

    if current_LED == new_LED:
        answer = current_click_count
        break

    if current_LED >= MAX_LED or current_click_count >= click_count:
        continue

    if is_enable_click_B(current_LED):
        LED_B = clickedB(current_LED)

        if visited[LED_B] > current_click_count+1:
            visited[LED_B] = current_click_count+1
            queue.append((LED_B, current_click_count+1))

    if current_LED+1 <= MAX_LED and visited[current_LED+1] > current_click_count+1:
        visited[current_LED+1] = current_click_count+1
        queue.append((current_LED+1, current_click_count+1))

print(answer)
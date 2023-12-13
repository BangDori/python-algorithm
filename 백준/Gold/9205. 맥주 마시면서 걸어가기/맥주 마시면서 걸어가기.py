from collections import deque
import sys
input = sys.stdin.readline

MAX_DISTANCE = 50 * 20

def get_distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

T = int(input())
for _ in range(T):
    store_count = int(input())

    house_x, house_y = map(int, input().split())
    store = [list(map(int, input().split())) for _ in range(store_count)]
    festival_x, festival_y = map(int, input().split())
    
    # 50m 마다 맥주마시기
    queue = deque([(house_x, house_y)])
    answer = "sad"
    while queue:
        x, y = queue.popleft()

        if get_distance(x, y, festival_x, festival_y) <= MAX_DISTANCE:
            answer = "happy"
            break

        removed = deque([])
        for index, coord in enumerate(store):
            store_x, store_y = coord
            if get_distance(x, y, store_x, store_y) <= MAX_DISTANCE:
                queue.append((store_x, store_y))
                removed.append(index)

        while removed:
            store.pop(removed.pop())

    print(answer)
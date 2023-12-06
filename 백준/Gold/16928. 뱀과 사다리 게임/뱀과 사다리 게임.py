from collections import deque
import sys
input = sys.stdin.readline

dice = [1, 2, 3, 4, 5, 6]
FINAL_DEST = 100

ladder_count, snake_count = map(int, input().split())
tp = {}

for _ in range(ladder_count):
    src, dst = map(int, input().split())
    tp[src] = dst

for _ in range(snake_count):
    src, dst = map(int, input().split())
    tp[src] = dst

# pos, count
queue = deque([(1, 0)])
visited = [False for _ in range(101)]
answer = 0
while queue:
    pos, count = queue.popleft()

    if pos == FINAL_DEST:
        answer = count
        break

    if tp.get(pos):
        queue.append((tp[pos], count))
        continue

    for move in dice:
        next = pos + move

        if 0 <= next <= FINAL_DEST and not visited[next]:
            if tp.get(next) and not visited[tp[next]]:
                visited[tp[next]] = True
                queue.append((tp[next], count+1))
            else:
                visited[next] = True
                queue.append((next, count+1))

print(answer)
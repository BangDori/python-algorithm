import sys
input = sys.stdin.readline

h, w = map(int, input().split())

blocks = list(map(int, input().split()))
answer = 0

blocks.append(-1)

for idx in range(1, len(blocks)-2):
    left_max = max(blocks[0:idx])
    right_max = max(blocks[idx+1:-1])
    required = min(left_max, right_max)

    if blocks[idx] <= required:
        answer += (required - blocks[idx])
print(answer)
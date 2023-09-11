import sys
input = sys.stdin.readline

item_count = int(input())
items = [int(input()) for _ in range(item_count)]
items.sort(reverse=True)

answer = 0
for idx, item in enumerate(items):
    if (idx+1) % 3 == 0:
        continue

    answer += item
print(answer)

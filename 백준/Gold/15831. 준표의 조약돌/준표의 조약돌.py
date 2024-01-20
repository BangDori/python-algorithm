import sys
input = sys.stdin.readline

WHITE = 'W'
BLACK = 'B'

total_count, max_b, min_w = map(int, input().split())
stone = input().strip()

left = 0
w_count = 0; b_count = 0
answer = 0

for right in range(total_count):
    if stone[right] == WHITE: w_count += 1
    else: b_count += 1

    # black 최대 개수 넘으면
    while b_count > max_b:
        if stone[left] == WHITE: w_count -= 1
        else: b_count -= 1

        left += 1

    if w_count >= min_w:
        answer = max(answer, right-left+1)

print(answer)
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
answer = []

for length in range(L, 101):
    middle = N // length
    left = middle - 1
    right = middle + 1

    current_sum = middle
    count = 1
    while current_sum < N:
        current_sum += right
        right += 1; count += 1
        if count >= length:
            break

        if left >= 0:
            current_sum += left
            left -= 1; count += 1
            if count >= length:
                break
    
    if current_sum == N and count >= L:
        answer.append(left+1)
        answer.append(right)
        break

if len(answer) == 0: print(-1)
else:
    for num in range(answer[0], answer[1]):
        print(num, end=' ')
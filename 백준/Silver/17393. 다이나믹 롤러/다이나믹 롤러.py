import sys
input = sys.stdin.readline

def get_paint_pos(current_pos, current_ink):
    left, right = current_pos+1, N-1
    pos = current_pos

    while left <= right:
        mid = (left + right) // 2

        if B[mid] <= current_ink:
            left = mid + 1
            pos = mid
        elif current_ink < B[mid]:
            right = mid - 1

    return pos

N = int(input())
A = list(map(int, input().split())) # 잉크 지수
B = list(map(int, input().split())) # 점도 지수

for i in range(N):
    current_ink = A[i]
    pos = get_paint_pos(i, A[i])

    print(pos-i, end=' ')

# 6
# 1 2 3 4 5 6
# 1 1 2 2 3 3
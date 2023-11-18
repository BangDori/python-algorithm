import sys
input = sys.stdin.readline

def binary_search(n, k):
    left = 0
    right = 5000

    while left <= right:
        mid = (left+right) // 2

        if mid * (mid+1) * k < 2 * n:
            left = mid+1
        else:
            right = mid-1
    
    return left
        
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())

    dir = binary_search(N, K)
    ans_dir = 'L' if dir % 2 == 0 else 'R'

    if dir % 2 == 0:
        pos = -K * ((dir + 1) // 2)
        pos -= N - 1 - (dir * (dir + 1) * K // 2)
    else:
        pos = K * ((dir + 1) // 2)
        pos += N - 1 - (dir * (dir + 1) * K // 2)

    print(pos, ans_dir)
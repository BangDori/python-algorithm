import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

def binary_search(N, K):
    left = 1
    right = K

    answer = 0
    while left <= right:
        # mid가 개수
        mid = (left+right) // 2

        count = 0
        for i in range(1, N+1):
            count += min(N, mid//i)

        if count >= K:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer

answer = binary_search(N, K)
print(answer)
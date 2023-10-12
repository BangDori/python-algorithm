import sys
input = sys.stdin.readline

def binary_search(num: int, A: list):
    min = 0
    max = len(A) - 1

    while min <= max:
        mid = (min + max) // 2

        if A[mid] == num:
            return 1
        elif A[mid] < num:
            min = mid + 1
        else:
            max = mid - 1
    
    return 0


N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
finds = list(map(int, input().split()))

for find in finds:
    print(binary_search(find, A))
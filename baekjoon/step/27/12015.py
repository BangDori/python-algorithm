import sys
input = sys.stdin.readline

size = int(input())
array = list(map(int, input().split()))

result = [array[0]]
for idx in range(1, len(array)):
    if result[-1] < array[idx]:
        result.append(array[idx])
        continue

    left = 0
    right = len(result)-1
    while left < right:
        mid = (left + right) // 2

        if result[mid] < array[idx]:
            left = mid + 1
        else:
            right = mid
    result[right] = array[idx]

print(len(result))
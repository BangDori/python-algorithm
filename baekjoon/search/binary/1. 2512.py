import sys
input = sys.stdin.readline

province = int(input())
requests = list(map(int, input().split()))
budget = int(input())

requests.sort()

left = 1
right = requests[-1]

accepted = []
while left <= right:
    mid = (left + right) // 2

    request_budget = 0
    for request in requests:
        request_budget += mid if request > mid else request
    
    if request_budget <= budget:
        accepted.append(mid)
        left = mid + 1
    else:
        right = mid - 1

print(accepted[-1])
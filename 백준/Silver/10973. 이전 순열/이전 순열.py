import sys
input = sys.stdin.readline

def solve(N, numbers):
    for i in range(N-1, 0, -1):
        
        if numbers[i] < numbers[i-1]:
            x, y = i-1, i

            for j in range(N-1, 0, -1):
                if numbers[j] < numbers[x]:
                    numbers[j], numbers[x] = numbers[x], numbers[j]
                    numbers = numbers[:i] + sorted(numbers[i:], reverse=True)
                    
                    return numbers

    return -1

N = int(input())
numbers = list(map(int, input().split()))

answer = solve(N, numbers)
if answer == -1: print(-1)
else: print(*answer)
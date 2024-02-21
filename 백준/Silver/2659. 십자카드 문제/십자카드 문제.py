from collections import deque

def findClockNumber(numbers):
    find = deque(numbers)
    clockNumber = 10000

    for _ in range(4):
        current = find[0] * 1000 + find[1] * 100 + find[2] * 10 + find[3]
        clockNumber = min(clockNumber, current)
        find.rotate(1)
    
    return clockNumber

numbers = list(map(int, input().split()))

clockNumber = findClockNumber(numbers)
start = 1111
answer = 0

while start <= clockNumber:
    currentNumbers = list(map(int, list(str(start))))
    if findClockNumber(currentNumbers) == start:
        answer += 1
    start += 1

print(answer)
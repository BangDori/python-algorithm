import sys
input = sys.stdin.readline

x = int(input())

answer = 0
for i in range(6, -1, -1):
    if x >= 2 ** i:
        x -= 2 ** i
        answer += 1
    
    if x == 0:
        break

print(answer)
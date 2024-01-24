import sys
input = sys.stdin.readline

row, col = map(int, input().split())

answer = 1
if row == 1: answer = 1
elif row == 2: answer = min(4, (col+1)//2)
elif col <= 6: answer = min(4, col)
else: answer = col-2

print(answer)
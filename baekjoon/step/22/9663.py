import sys
input = sys.stdin.readline

N = int(input())
chess = [0] * N
answer = 0

def isPutQueen(row: int):
    for r in range(row):
        if (chess[row] == chess[r]) or (abs(chess[row] - chess[r]) == abs(row - r)):
            return False
    
    return True

def dfs(row: int):
    global answer
    if row == N:
        answer += 1
        return
    
    for col in range(0, N):
        chess[row] = col

        if isPutQueen(row):
            dfs(row+1)

dfs(0)
print(answer)
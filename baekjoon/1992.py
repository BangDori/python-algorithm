import sys
input = sys.stdin.readline

N = int(input())
video = [list(map(int, input().rstrip())) for _ in range(N)]

answer = ""

def dfs(row, col, size):
    global answer
    num = video[row][col]
    isSame = True

    for r in range(row, row+size):
        for c in range(col, col+size):
            if num != video[r][c]:
                isSame = False
                break
    
    if isSame or size == 1:
        answer += str(num)
        return
    
    size //= 2
    answer += '('
    dfs(row, col, size)
    dfs(row, col+size, size)
    dfs(row+size, col, size)
    dfs(row+size, col+size, size)
    answer += ')'

dfs(0, 0, N)
print(answer)
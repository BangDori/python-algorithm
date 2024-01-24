import sys
input = sys.stdin.readline

def is_valid_sqaure(size):
    for r in range(row-size):
        for c in range(col-size):
            if board[r][c] == board[r+size][c] == board[r][c+size] == board[r+size][c+size]:
                return True
    
    return False

row, col = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(row)]

size = 1
answer = -1
while size+1 <= min(row, col):
    is_sqaure = is_valid_sqaure(size)
    if is_sqaure: answer = size+1
    size += 1
                
print(answer*answer)
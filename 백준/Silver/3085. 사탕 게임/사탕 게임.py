import sys
input = sys.stdin.readline

size = int(input())
board = [list(input().rstrip()) for _ in range(size)]

dr = [0, 1]
dc = [1, 0]

def get_max_length():
    length = 0

    for r in range(size):
        cnt = 1

        for c in range(1, size):
            if board[r][c] == board[r][c-1]:
                cnt += 1
            else:
                length = max(length, cnt)
                cnt = 1

        length = max(length, cnt)
    
    for c in range(size):
        cnt = 1

        for r in range(1, size):
            if board[r][c] == board[r-1][c]:
                cnt += 1
            else:
                length = max(length, cnt)
                cnt = 1
    
        length = max(length, cnt)
    
    return length

answer = 0
for row in range(size):
    for col in range(size):

        for i in range(2):
            nr = row + dr[i]
            nc = col + dc[i]

            if nr < size and nc < size:
                board[nr][nc], board[row][col] = board[row][col], board[nr][nc]
                r_cnt, c_cnt = 0, 0

                answer = max(answer, get_max_length())
                board[nr][nc], board[row][col] = board[row][col], board[nr][nc]

print(answer)
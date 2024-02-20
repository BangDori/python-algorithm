SIZE = 5; MAX_DIGIT = 6

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(row, col, number, digit):
    if digit == MAX_DIGIT:
        unique_numbers.add(number)
        return
    
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]

        if 0 <= nr < SIZE and 0 <= nc < SIZE:
            dfs(nr, nc, number * 10 + board[nr][nc], digit+1)

    return

board = [list(map(int, input().split())) for _ in range(SIZE)]
unique_numbers = set()

for row in range(SIZE):
    for col in range(SIZE):
        dfs(row, col, board[row][col], 1)

print(len(unique_numbers))
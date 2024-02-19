# 행을 max로 잡을 경우 60 * 70 = 4200
# 열을 max로 잡을 경우 80 * 50 = 4000

def solution(sizes):
    answer = 0
    
    max_row = 0; max_col = 0
    for row, col in sizes:
        max_row = max(max_row, row)
        max_col = max(max_col, col)
    
    min_col = 0
    for row, col in sizes:
        if row == max_row: min_col = max(min_col, col)
        min_size = min(row, col)
        min_col = max(min_col, min_size)

    min_row = 0
    for row, col in sizes:
        if col == max_col: min_row = max(min_row, row)
        min_size = min(row, col)
        min_row = max(min_row, min_size)
    
    return max(max_row * min_col, min_row * max_col)
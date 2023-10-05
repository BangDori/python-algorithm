import sys
input = sys.stdin.readline

find_alphabet = list(input().rstrip())
rows, cols = map(int, input().rstrip().split())
alphabet_table = [list(input().rstrip()) for _ in range(rows)]

answer = 0
def dfs(row, col, cur, check, init):
    if cur == len(find_alphabet):
        global answer
        answer = 1
        return 1
    
    if check >= 8:
        return 0
        
    if check == 0:
        # Top
        if col+1 <= cols-1 and alphabet_table[row][col+1] == find_alphabet[cur]:
            dfs(row, col+1, cur+1, check, init)
        else:
            dfs(init[0], init[1], 1, check+1, init)
    elif check == 1:
        # Right
        if row+1 <= rows-1 and alphabet_table[row+1][col] == find_alphabet[cur]:
            dfs(row+1, col, cur+1, check, init)
        else:
            dfs(init[0], init[1], 1, check+1, init)
    elif check == 2:
        # Bottom
        if col-1 >= 0 and alphabet_table[row][col-1] == find_alphabet[cur]:
            dfs(row, col-1, cur+1, check, init)
        else:
            dfs(init[0], init[1], 1, check+1, init)
    elif check == 3:
        # Left
        if row-1 >= 0 and alphabet_table[row-1][col] == find_alphabet[cur]:
            dfs(row-1, col, cur+1, check, init)
        else:
            dfs(init[0], init[1], 1, check+1, init)
    elif check == 4:
        # Left Top
        if row-1 >= 0 and col-1 >= 0 and alphabet_table[row-1][col-1] == find_alphabet[cur]:
            dfs(row-1, col-1, cur+1, check, init)
        else:
            dfs(init[0], init[1], 1, check+1, init)
    elif check == 5:
        # Right Top
        if row-1 >= 0 and col+1 <= cols-1 and alphabet_table[row-1][col+1] == find_alphabet[cur]:
            dfs(row-1, col+1, cur+1, check, init)
        else:
            dfs(init[0], init[1], 1, check+1, init)
    elif check == 6:
        # Right Bottom
        if row+1 <= rows-1 and col+1 <= cols-1 and alphabet_table[row+1][col+1] == find_alphabet[cur]:
            dfs(row+1, col+1, cur+1, check, init)
        else:
            dfs(init[0], init[1], 1, check+1, init)
    elif check == 7:
        # Left Bottom
        if row+1 <= rows-1 and col-1 >= 0 and alphabet_table[row+1][col-1] == find_alphabet[cur]:
            dfs(row+1, col-1, cur+1, check, init)
        else:
            dfs(init[0], init[1], 1, check+1, init)
    
    return 0


if len(find_alphabet) > rows and len(find_alphabet) > cols:
    print(0)
else:
    for row in range(rows):
        for col in range(cols):
            if alphabet_table[row][col] != find_alphabet[0]:
                continue

            isFind = dfs(row, col, 1, 0, (row, col))

            if answer == 1:
                print(1)
                sys.exit(0)

    print(0)
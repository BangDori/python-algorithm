import sys
input = sys.stdin.readline

row, col = map(int, input().split())
puzzle = [list(input().strip()) for _ in range(row)]
visited = [[[False, False] for _ in range(col)] for _ in range(row)]

words = []

for r in range(row):
    for c in range(col):
        if puzzle[r][c] == '#' or (visited[r][c][0] == True and visited[r][c][1] == True): continue

        # right
        word = puzzle[r][c]
        visited[r][c][0] = True

        nc = c
        while True:
            nc += 1

            if 0 <= nc < col and not visited[r][nc][0] and puzzle[r][nc] != '#':
                visited[r][nc][0] = True
                word += puzzle[r][nc]
            else:
                if len(word) > 1: words.append(word)
                break

        # bottom
        word = puzzle[r][c]
        visited[r][c][1] = True

        nr = r
        while True:
            nr += 1

            if 0 <= nr < row and not visited[nr][c][1] and puzzle[nr][c] != '#':
                visited[nr][c][1] = True
                word += puzzle[nr][c]
            else:
                if len(word) > 1: words.append(word)
                break

words.sort(reverse=True)
print(words.pop())
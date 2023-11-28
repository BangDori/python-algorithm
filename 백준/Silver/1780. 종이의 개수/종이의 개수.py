import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

answer = [0, 0, 0]

def isEnableCheck(row, col, size):
    paper_numbers = set()

    for x in range(row, row+size):
        for y in range(col, col+size):
            paper_numbers.add(paper[x][y])

    if len(paper_numbers) == 1:
        answer[paper_numbers.pop()+1] += 1
        return True
    
    return False

def cut(row, col, size):
    isEnable = isEnableCheck(row, col, size)

    if isEnable:
        return

    for x in range(row, row+size, size//3):
        for y in range(col, col+size, size//3):
            cut(x, y, size//3)


size = int(input())
paper = [list(map(int, input().split())) for _ in range(size)]

cut(0, 0, size)
for ans in answer:
    print(ans)
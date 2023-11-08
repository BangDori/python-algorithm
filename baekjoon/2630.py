import sys
input = sys.stdin.readline

white_paper = 0
blue_paper = 0

def insicion(x, y, side):
    global white_paper, blue_paper

    tot = 0

    for row in range(x, x+side):
        for col in range(y, y+side):
            tot += matrix[row][col]

    if tot == 0:
        white_paper += 1
        return

    if tot == side**2:
        blue_paper += 1
        return

    insicion(x, y, side//2)
    insicion(x, y+side//2, side//2)
    insicion(x+side//2, y, side//2)
    insicion(x+side//2, y+side//2, side//2)

side = int(input())
matrix = [list(map(int, input().split())) for _ in range(side)]

insicion(0, 0, side)

print(white_paper)
print(blue_paper)
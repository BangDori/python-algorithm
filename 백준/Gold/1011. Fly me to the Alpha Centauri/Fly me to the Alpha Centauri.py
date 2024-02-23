import sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    x, y = map(int, input().split())

    move = y - x
    moves = int(move ** 0.5)
    cnt = moves

    if move > moves * moves:
        nextX = moves

        while nextX < move and nextX < 2147483647:
            nextX += moves
            cnt += 1
    
    elif move == moves * moves:
        cnt = 2 * moves - 1
    
    print(cnt)
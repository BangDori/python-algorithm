table = [[0 for _ in range(11)] for _ in range(11)]

ant_x = 2 # 개미의 x좌표
ant_y = 2 # 개미의 y좌표

food_cnt = 0 # 먹이의 개수
food_x = 0 # 먹이의 x좌표
food_y = 0 # 먹이의 y좌표

for i in range(1, 11):
    table[i] = list(map(int, input().split()))
    table[i].insert(0, 0)

for i in range(2, 10):
    for j in range(2, 10):
        if(int(table[i][j]) == 2):
            food_cnt += 1
            food_x = j
            food_y = i

while food_cnt > 0:
    table[ant_y][ant_x] = 9

    if (ant_x == 9) & (ant_y == 9):
        break

    if (ant_x == food_x) & (ant_y == food_y):
        break

    if (table[ant_y][ant_x+1] != 1):
        ant_x += 1
        continue

    if (table[ant_y+1][ant_x] != 1):
        ant_y += 1
        continue

    break

for i in range(1, 11):
    for j in range(1, 11):
        print(table[i][j], end=' ')
    print()

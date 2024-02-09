import sys
input = sys.stdin.readline

# direction, row, col
dirs = [['R', 0, 1], ['L', 0, -1], ['B', 1, 0], ['T', -1, 0], ['RT', -1, 1], ['LT', -1, -1], ['RB', 1, 1], ['LB', 1, -1]]
chess = [[0] * 8 for _ in range(8)]

king, stone, move_cnt = input().strip().split()
moving = [input().rstrip() for _ in range(int(move_cnt))]

def convert_coordinate_for_item(item):
    alpha, num = item[0], item[1]

    return 8-int(num), ord(alpha)-ord('A')

def convert_item_for_coordinate(row, col):
    answer = [chr(ord('A')+col), str(8-row)]
    return "".join(answer)

k_row, k_col = convert_coordinate_for_item(king)
s_row, s_col = convert_coordinate_for_item(stone)

chess[k_row][k_col] = 1
chess[s_row][s_col] = 2

for move in moving:
    for dir, dr, dc in dirs:
        if dir == move:
            k_nr = k_row + dr
            k_nc = k_col + dc

            # king 이동 가능
            if 0 <= k_nr < 8 and 0 <= k_nc < 8:
                if chess[k_nr][k_nc] == 2: # stone 이라면
                    s_nr = s_row + dr
                    s_nc = s_col + dc

                    # stone 이동 가능
                    if 0 <= s_nr < 8 and 0 <= s_nc < 8:
                        chess[s_nr][s_nc] = 2
                        chess[k_nr][k_nc] = 1

                        k_row, k_col = k_nr, k_nc
                        s_row, s_col = s_nr, s_nc
                else:
                    chess[k_nr][k_nc] = 1
                    k_row, k_col = k_nr, k_nc

            break

print(convert_item_for_coordinate(k_row, k_col))
print(convert_item_for_coordinate(s_row, s_col))
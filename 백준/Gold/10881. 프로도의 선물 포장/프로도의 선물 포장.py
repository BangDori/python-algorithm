import sys
input = sys.stdin.readline

GIFT_COUNT = 3
BOXES = 6
TC = int(input())

# TC <= 10,000
# GIFT_BOX <= 100*100

# 3*4,5*6, 4*1
# 354 454, ?
# 10 * 5 = 5 + (4+6)
# (3+5)*()

def get_min_size():
    answer = sys.maxsize

    for i in range(BOXES): # 1
        for j in range(BOXES): # 2
            for k in range(BOXES): # 3
                if i//2 == j//2 or j//2 == k//2 or k//2 == i//2:
                    continue

                # 한 줄
                row1 = gifts[i][0] + gifts[j][0] + gifts[k][0]
                col1 = max(gifts[i][1], gifts[j][1], gifts[k][1])

                # 두 줄
                row2 = max(gifts[i][0] + gifts[j][0], gifts[k][0])
                col2 = max(gifts[i][1], gifts[j][1]) + gifts[k][1]

                answer = min(answer, row1*col1, row2*col2)

    return answer            

for _ in range(TC):
    gifts = []

    for _ in range(GIFT_COUNT):
        row, col = map(int, input().split())

        # 회전 포함
        gifts.append((row, col))
        gifts.append((col, row))

    answer = get_min_size()
    print(answer)
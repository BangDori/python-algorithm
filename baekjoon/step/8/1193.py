x = int(input())

# floor = 1, 1/1
# floor = 2, 1/2 2/1
# floor = 3, 1/3 2/2 3/1
floor = 1
tot = 0

while x > tot: # 해당 floor에 도착할 때까지
    tot += floor
    floor += 1

# floor 한칸 낮추기
floor -= 1
tot -= floor

# 지그재그 형식으로 추력
if floor % 2 == 0:
    print('%d/%d' % (x-tot, (floor+1)-(x-tot)))
else:
    print('%d/%d' % ((floor+1)-(x-tot), x-tot))
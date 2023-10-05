import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    max_money = 5 * (10 ** 6)
    grounds = []

    # 입력
    while True:
        ground = int(input())

        if ground == 0:
            break
        grounds.append(ground)
    
    # 정렬
    grounds.sort(reverse=True)

    # 계산
    need_money = 0
    for idx, ground in enumerate(grounds):
        need_money += 2 * (ground ** (idx+1))
    
    # 출력
    if need_money <= max_money:
        print(need_money)
    else:
        print("Too expensive")
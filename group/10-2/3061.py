import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    ladder_count = int(input())

    origin = [i+1 for i in range(ladder_count)]
    ladder = list(map(int, input().split()))
    answer = 0

    for i in range(ladder_count):
        if ladder[i] == origin[i]:
            continue

        pos_i = ladder.index(origin[i])
        for j in range(pos_i, i, -1):
            ladder[j] = ladder[j-1]
        
        ladder[i] = origin[i]
        answer += (pos_i - i)
    #     print("[MOVE]", ladder, answer)
    # print("[RESERT]", ladder)
    print(answer)
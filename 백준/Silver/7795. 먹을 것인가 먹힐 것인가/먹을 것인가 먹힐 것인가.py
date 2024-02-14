import sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    a_cnt, b_cnt = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    b = sorted(list(map(int, input().split())), reverse=True)

    ptr_a = 0; ptr_b = 0
    answer = 0

    while ptr_a < a_cnt and ptr_b < b_cnt:
        if a[ptr_a] > b[ptr_b]:
            answer += b_cnt - ptr_b
            ptr_a += 1
        else:
            ptr_b += 1
    
    print(answer)
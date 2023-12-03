import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    clothes_count = int(input())
    clothes = {}

    answer = 1
    for _ in range(clothes_count):
        name, clothes_type = input().split()

        if not clothes.get(clothes_type):
            clothes[clothes_type] = 0
        clothes[clothes_type] += 1
    
    for count in clothes.values():
        answer *= (count+1)
    
    print(answer-1)
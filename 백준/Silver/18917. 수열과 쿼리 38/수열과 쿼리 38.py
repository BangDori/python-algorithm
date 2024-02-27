import sys
input = sys.stdin.readline

query_count = int(input())

curr_sum = 0
curr_xor = 0
for _ in range(query_count):
    commands = list(map(int, input().split()))

    if commands[0] == 1: 
        curr_sum += commands[1]
        curr_xor ^= commands[1]
    elif commands[0] == 2:
        curr_sum -= commands[1]
        curr_xor ^= commands[1]
    elif commands[0] == 3: print(curr_sum)
    else: print(curr_xor)
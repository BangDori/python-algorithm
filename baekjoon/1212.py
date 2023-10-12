import sys
input = sys.stdin.readline

num2 = ['000', '001', '010', '011', '100', '101', '110', '111', '1000']

num8 = list(map(int, input().rstrip()))

for idx, num in enumerate(num8):
    if idx == 0:
        print(int(num2[num]), end='')
        continue
    print(num2[num], end='')
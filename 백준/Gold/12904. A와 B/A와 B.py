import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

S = list(input().strip())
T = list(input().strip())

is_flag = False
while T:
    if T[-1] == 'A':
        T.pop()
    else:
        T.pop()
        T.reverse()
    
    if S == T:
        is_flag = True
        break

print(1 if is_flag else 0)
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

def dfs(cur, count):
    if count == M-1:
        for ans in cur:
            print(ans, end=' ')
        print()
        return
    
    for num in array:
        if num >= cur[-1]:
            dfs(cur + [num], count+1)

for num in array:
    dfs([num], 0)
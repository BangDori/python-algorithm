import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())
array = [i for i in range(N+1)]

def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        array[b] = a
    else:
        array[a] = b

def find(i):
    if array[i] == i:
        return i
    array[i] = find(array[i])    
    return find(array[i])

for _ in range(M):
    command, a, b = map(int, input().split())

    if command == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
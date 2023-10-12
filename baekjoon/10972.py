import sys
input = sys.stdin.readline

def next_permutation(array):
    x = 0
    for idx in range(1, len(array)):
        if array[idx] > array[idx-1]:
            x = idx-1
    
    y = x
    for idx in range(x+1, len(array)):
        if array[idx] > array[x]:
            y = idx

    if x == 0 and y == 0:
        return False
    
    array[x], array[y] = array[y], array[x]

    array_cp = array[x+1:].copy()
    array_cp.reverse()
    array = array[:x+1] + array_cp

    return array

N = int(input())
array = list(map(int, input().split()))

answer = next_permutation(array)

if not answer:
    print(-1)
else:
    for ans in answer:
        print(ans, end=' ')
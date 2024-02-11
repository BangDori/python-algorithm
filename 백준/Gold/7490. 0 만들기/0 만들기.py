import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(curr, tot):
    global answer
    if curr >= N:
        # print(curr, numbers)
        if curr == N and tot == 0:
            answer.append("".join(numbers))
        return
    
    numbers.append('+' + str(curr+1))
    dfs(curr+1, tot+curr+1)
    numbers.pop()

    if curr != 0:
        numbers.append(str(-(curr+1)))
        dfs(curr+1, tot-(curr+1))
        numbers.pop()

    if curr - 2 <= N:
        numbers.append('+' + str(curr+1) + ' ' + str(curr+2))
        dfs(curr+2, tot + (curr+1) * 10 + curr+2)
        numbers.pop()

        if curr != 0:
            numbers.append('-' + str(curr+1) + ' ' + str(curr+2))
            dfs(curr+2, tot - ((curr+1) * 10 + curr+2))
            numbers.pop()
    

TC = int(input())
for _ in range(TC):
    N = int(input())

    numbers = []
    answer = []
    dfs(0, 0)

    answer.sort()
    for ans in answer:
        print(ans[1:])
    print()
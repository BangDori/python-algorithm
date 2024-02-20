import sys
input = sys.stdin.readline

def dfs(index, current_shin, current_ssen, is_used):
    global answer
    if index == N:
        if not is_used: return
        answer = min(answer, abs(current_shin - current_ssen))
        return

    dfs(index+1, current_shin * food[index][0], current_ssen + food[index][1], True)
    dfs(index+1, current_shin, current_ssen, is_used)

N = int(input())
food = []
answer = sys.maxsize

for _ in range(N):
    shin, ssen = map(int, input().split())
    food.append((shin, ssen))

dfs(0, 1, 0, False)
print(answer)
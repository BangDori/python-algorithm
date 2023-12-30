import sys
input = sys.stdin.readline

def solve(current_string):
    global answer
    if len(current_string) == 0:
        answer = 1
        return
    
    if visited.get(current_string):
        return
    visited[current_string] = 1

    idx = 0
    while idx < len(current_string):
        count = 1
        while idx + count < len(current_string) and current_string[idx] == current_string[idx + count]:
            count += 1

        if count >= 2:
            next_string = current_string[:idx] + current_string[idx+count:]
            solve(next_string)
        
        if count == 1:
            idx += 1
        else:
            idx = idx+count

TC = int(input())
for _ in range(TC):
    input_string = input().rstrip()
    answer = 0
    visited = {}

    solve(input_string)
    print(answer)
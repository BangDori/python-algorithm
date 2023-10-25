import sys
input = sys.stdin.readline

start = input().rstrip()
end = input().rstrip()

def dfs(temp):
    if temp == start:
        print(1)
        sys.exit(0)
    
    if len(temp) <= len(start):
        return

    if temp[-1] == 'A':
        dfs(temp[:-1])
    
    if temp[0] == 'B':
        dfs(temp[1:][::-1])

dfs(end)
print(0)
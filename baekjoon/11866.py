import sys
input = sys.stdin.readline

# N 명의 사람
# K 번째 제거
N, K = map(int, input().split())

table = [i for i in range(1, N+1)]
yo = []

count = 1
next = 0

while len(yo) < N-1:
    if count == K:
        user = table[next]
        yo.append(str(user))
        table.remove(user)
        count = 1
        next = next % len(table)
    else:
        count += 1
        next = (next + 1) % len(table)

yo.append(str(table.pop()))

print("<", end="")
print(", ".join(yo), end="")
print(">", end="")
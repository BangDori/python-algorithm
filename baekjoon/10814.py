# 회원의 수 (N)
N = int(input())
members = [() for _ in range(N)]

for i in range(N):
    x, y = input().split()
    x = int(x)

    members[i] = x, y

members.sort(key= lambda member : member[0])

for i in range(N):
    print(members[i][0], members[i][1])
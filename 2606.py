import sys
input = sys.stdin.readline

computer_count = int(input())
connection_count = int(input())
warm_virus = [0 for _ in range(computer_count+1)]

network = {}

for _ in range(connection_count):
    x, y = map(int, input().split())

    if not network.get(x):
        network[x] = []
    if not network.get(y):
        network[y] = []

    network[x].append(y)
    network[y].append(x)

def dfs(computer):
    warm_virus[computer] = 1
    connection_list = network.get(computer, [])

    for connection in connection_list:
        if warm_virus[connection] == 1:
            continue

        dfs(connection)

dfs(1)
print(warm_virus.count(1)-1)
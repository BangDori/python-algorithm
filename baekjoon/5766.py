import sys
input = sys.stdin.readline

while True:
    rows, count = map(int, input().split())

    if rows == 0 and count == 0:
        break

    bridge = {}

    for _ in range(rows):
        ranking = list(map(int, input().split()))

        for user in ranking:
            if not bridge.get(user):
                bridge[user] = 0
            
            bridge[user] += 1

    users = [(user, bridge.get(user)) for user in list(bridge.keys())]

    users.sort(reverse=True,key=lambda val: (val[1], -val[0]))
    max_point = users[0][1]

    while True:
        if users[0][1] == max_point:
            users.pop(0)
        else:
            break

    second_point = users[0][1]
    for user, point in users:
        if point == second_point:
            print(user, end=' ')
        else:
            break
    print()
import sys
input = sys.stdin.readline

player_count, room_count = map(int, input().split())

rooms = []

for _ in range(player_count):
    player_level, player_name = input().split()
    player_level = int(player_level)

    if len(rooms) == 0:
        rooms.append([(player_level, player_name)])
        continue
    
    isEnter = False
    for idx in range(len(rooms)):
        if len(rooms[idx]) == room_count:
            continue

        if rooms[idx][0][0] - 10 <= player_level <= rooms[idx][0][0] + 10:
            rooms[idx].append((player_level, player_name))
            isEnter = True
            break

    if not isEnter:
        rooms.append([(player_level, player_name)])

for room in rooms:
    if len(room) == room_count:
        print("Started!")
    else:
        print("Waiting!")
    
    room.sort(key=lambda v: v[1])
    for level, name in room:
        print(level, name)

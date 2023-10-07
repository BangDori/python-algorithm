import sys, itertools
input = sys.stdin.readline

door_count = int(input())
water_doors = []
tot_doors = []

for _ in range(door_count):
    flux, cost = map(int, input().split())

    water_doors.append((flux, cost))

for count in range(1, door_count+1):
    for doors in itertools.combinations(water_doors, count):
        tot_flux = 0; tot_cost = 0

        for door in doors:
            tot_flux += door[0]
            tot_cost += door[1]
            
        tot_doors.append((tot_flux, tot_cost))

tot_doors.sort(key=lambda val: val[1])

test_case = int(input())
for idx in range(test_case):
    water, hour = map(int, input().split())
    answer = 0

    for door in tot_doors:
        if door[0] * hour >= water:
            answer = door[1]
            break
    
    if answer == 0:
        print("Case %d: IMPOSSIBLE" % (idx+1))
    else:
        print("Case %d: %d" % (idx+1, answer))
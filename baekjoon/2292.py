n = int(input())

floor = 1
tot = 1

while n > tot:
    tot += (6 * floor)
    floor += 1

print(floor)
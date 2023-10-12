import sys
input = sys.stdin.readline

drint_count = int(input())
drinks = list(map(int, input().split()))
drinks.sort()

total_drink = drinks.pop()

for drink in drinks:
    total_drink += (drink / 2)

if total_drink - int(total_drink) == 0:
    print(int(total_drink))
else:
    print("%.1f" % total_drink)
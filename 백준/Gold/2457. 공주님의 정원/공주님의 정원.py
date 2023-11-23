import sys
input = sys.stdin.readline

START = 301
END = 1130

N = int(input())
flowers = []

for _ in range(N):
    month1, day1, month2, day2 = map(int, input().split())
    date1 = month1 * 100 + day1
    date2 = month2 * 100 + day2

    flowers.append((date1, date2))

count = 0
target = START

flowers.sort(key=lambda v: (v[0], v[1]))

while flowers:
    end = 0

    if target > END or target < flowers[0][0]:
        break

    while flowers:
        if target >= flowers[0][0]:
            if end <= flowers[0][1]:
                end = flowers[0][1]
            
            flowers.pop(0)
        else:
            break
    
    target = end
    count += 1

if target > END:
    print(count)
else:
    print(0)
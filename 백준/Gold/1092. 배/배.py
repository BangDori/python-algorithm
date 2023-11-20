import sys
input = sys.stdin.readline

crane_count = int(input())
cranes = list(map(int, input().split()))
box_count = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

time = 0

if boxes[0] > cranes[0]:
    time = -1
else:
    while boxes:
        for crane in cranes:
            if boxes and crane < boxes[-1]:
                continue

            for b in boxes:
                if crane >= b:
                    boxes.remove(b)
                    break

        time += 1

print(time)
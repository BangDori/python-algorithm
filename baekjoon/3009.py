point1 = list(map(int, input().split()))
point2 = list(map(int, input().split()))
point3 = list(map(int, input().split()))

x = 0
y = 0

if point1[0] == point2[0]:
    x = point3[0]
elif point1[0] == point3[0]:
    x = point2[0]
else:
    x = point1[0]

if point1[1] == point2[1]:
    y = point3[1]
elif point1[1] == point3[1]:
    y = point2[1]
else:
    y = point1[1]

print(x, y)
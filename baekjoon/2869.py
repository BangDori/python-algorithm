import math

# 하루에 올라가는 높이 (a), 미끄러지는 높이 (b), 높이 (v)
a, b, v = map(int, input().split())
v -= a

print(math.ceil(v / (a - b)) + 1)
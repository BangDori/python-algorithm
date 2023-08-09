h, m = map(int, input().split())
t = int(input())

m += t

if m >= 60:
    time_m = m // 60
    h += time_m
    m -= (time_m * 60)

if h >= 24:
    h -= 24

print(h, m)
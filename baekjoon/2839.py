import sys

N = int(input())

bag5 = N // 5 # 5키로 가방
bag3 = 0 # 3키로 가방

min = sys.maxsize
while bag5 >= 0:
    bag3 = (N - (bag5 * 5)) // 3

    if bag5*5 + bag3*3 == N and bag5 + bag3 < min:
        min = bag5 + bag3
    
    bag5 -= 1

if min == sys.maxsize:
    print(-1)
else:
    print(min)
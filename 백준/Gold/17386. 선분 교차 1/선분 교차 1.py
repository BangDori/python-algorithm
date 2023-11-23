import sys
input = sys.stdin.readline

def ccw(p1,p2,p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    A = x1*y2 + x2*y3 + x3*y1
    B = x2*y1 + x3*y2 + x1*y3

    if A - B > 0: # 반시계방향
        return 1
    elif A - B < 0: # 시계방향
        return -1
    else:
        return 0

x1,y1, x2,y2 = map(int,input().split())
x3,y3, x4,y4 = map(int,input().split())

P1 = (x1, y1)
P2 = (x2, y2)
P3 = (x3, y3)
P4 = (x4, y4)

res1 = ccw(P1, P2, P3) * ccw(P1, P2, P4)
res2 = ccw(P3, P4, P1) * ccw(P3, P4, P2)

if res1 == -1 and res2 == -1:
    print(1)
else:
    print(0)
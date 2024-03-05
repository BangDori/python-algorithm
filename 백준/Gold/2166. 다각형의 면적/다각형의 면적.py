# https://ko.wikihow.com/%EB%8B%A4%EA%B0%81%ED%98%95-%EB%84%93%EC%9D%B4-%EA%B5%AC%ED%95%98%EA%B8%B0#.EB.B3.80.EC.9D.98-.EA.B8.B8.EC.9D.B4.EA.B0.80-.EB.8B.A4.EB.A5.B8-.EB.8B.A4.EA.B0.81.ED.98.95-.EB.84.93.EC.9D.B4-.EA.B5.AC.ED.95.98.EA.B8.B0

import sys
input = sys.stdin.readline

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
points.append(points[0])

nx, ny = 0, 0
for i in range(len(points)-1):
    nx += points[i][0] * points[i+1][1]
    ny += points[i][1] * points[i+1][0]

print(round(abs(nx-ny)/2, 1))
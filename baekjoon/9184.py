"""
    1 sec, 128 MB

    재귀함수 w(a, b, c) -> DP로 변환

    -50 <= a, b, c <= 50
"""
import sys
input = sys.stdin.readline

result = [[[0 for _ in range(51)] for _ in range(51)] for _ in range(51)]

def w(A, B, C):    
    for a in range(A+1):
        for b in range(B+1):
            for c in range(C+1):
                if a == 0 or b == 0 or c == 0:
                    result[a][b][c] = 1
                    continue
                
                if a < b and b < c:
                    result[a][b][c] = result[a][b][c-1] + result[a][b-1][c-1] - result[a][b-1][c]
                    continue
                
                result[a][b][c] = result[a-1][b][c] + result[a-1][b-1][c] + result[a-1][b][c-1] - result[a-1][b-1][c-1]
    
    return result[a][b][c]

while True:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break
    
    w_result = 0
    if a <= 0 or b <= 0 or c <= 0:
        w_result = 1
    elif a > 20 or b > 20 or c > 20:
        w_result = w(20, 20, 20)
    else:
        w_result = w(a, b, c)
    print("w(%d, %d, %d) = %d" % (a, b, c, w_result))
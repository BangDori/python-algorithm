import sys
input = sys.stdin.readline

N = int(input())
antena = list(map(int, input().split()))
antena.sort()

print(antena[(N-1) // 2])
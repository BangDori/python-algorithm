import sys
input = sys.stdin.readline

n = int(input())
array = [0 for _ in range(n)]

for i in range(n):
    array[i] = int(input())

array.sort()
for i in range(n):
    print(array[i])
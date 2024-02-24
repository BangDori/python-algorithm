import sys
input = sys.stdin.readline

N = int(input())
trees = list(map(int, input().split()))
trees.sort(reverse=True)

answer = 0
for day, tree in enumerate(trees):
    answer = max(answer, tree + (day + 1) + 1)

print(answer)
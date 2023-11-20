import sys
input = sys.stdin.readline

N = int(input())
listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

listA.sort()
listB.sort(reverse=True)

answer = 0
for a, b in zip(listA, listB):
    answer += a * b
print(answer)
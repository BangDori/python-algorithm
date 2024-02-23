import sys
input = sys.stdin.readline

S = input().strip()
answer = []

for i in range(len(S)):
    answer.append(S[i:])

answer.sort()
for ans in answer:
    print(ans)
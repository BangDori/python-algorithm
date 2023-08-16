import sys
input = sys.stdin.readline

# 포켓몬의 수 (N), 문제의 수 (M)
N, M = map(int, input().split())
pocketmons = {}

for i in range(1, N+1):
    pocketmon = input().rstrip()
    pocketmons[i] = pocketmon
    pocketmons[pocketmon] = i

for i in range(M):
    quiz = input().rstrip()

    if quiz.isalpha():
        print(pocketmons.get(quiz))
    else:
        print(pocketmons.get(int(quiz)))
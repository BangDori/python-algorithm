# 듣도 못한 사람의 수 (N)
# 보도 못한 사람의 수 (M)
N, M = map(int, input().split())
humans = {}
real = []

for i in range(N):
    human = input()
    humans[human] = 1

for i in range(M):
    human = input()

    if humans.get(human):
        real.append(human)

real.sort()
print(len(real))
for i in range(len(real)):
    print(real[i])
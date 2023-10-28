from itertools import combinations, permutations
import sys
input = sys.stdin.readline

size = int(input())
table = [list(map(int, input().split())) for _ in range(size)]
people = [idx for idx in range(size)]

A_team = []
B_team = []

for i in range(2, size//2+1):
    A_temp = []
    B_temp = []

    for team in combinations(people, i):
        A_temp.append(team)
    
    for team in combinations(people, size-i):
        B_temp.append(team)

    A_team += A_temp
    B_temp.reverse()
    B_team += B_temp

answer = sys.maxsize
for i in range(len(A_team)):
    sub_A = 0
    sub_B = 0

    for x, y in permutations(A_team[i], 2):
        sub_A += table[x][y]
    
    for x, y in permutations(B_team[i], 2):
        sub_B += table[x][y]

    diff = abs(sub_A - sub_B)
    answer = min(answer, diff)

    if answer == 0:
        break

print(answer)
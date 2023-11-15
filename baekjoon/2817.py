import sys
input = sys.stdin.readline

people = int(input())
staff_count = int(input())
staffs = []

for _ in range(staff_count):
    name, votes = input().rstrip().split()
    votes = int(votes)

    if votes >= people * 0.05:
        staffs.append((name, votes))

FIRST_RANK = 1
LAST_RANK = 15

rank_dict = {}
staff_scores = []
for name, votes in staffs:
    rank_dict[name] = 0
    for i in range(FIRST_RANK, LAST_RANK):
        staff_scores.append((name, votes // i))
staff_scores.sort(key=lambda v: -v[1])

for rank in range(LAST_RANK-1):
    name, votes = staff_scores[rank]
    
    rank_dict[name] += 1

names = list(rank_dict.keys())
names.sort()

for name in names:
    print(name, rank_dict[name])
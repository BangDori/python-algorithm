import sys
input = sys.stdin.readline

country_count, country_num = map(int, input().split())

country_list = []
country_rank = {}

for _ in range(country_count):
    medal_list = list(map(int, input().rstrip().split()))
    medal_list.append(medal_list.pop(0))
    country_list.append(medal_list)

country_list.sort(reverse=True)

rank = 1
country_rank[country_list[0][-1]] = rank
acc = 1
for id in range(1, country_count):
    prev_gold, prev_silver, prev_bronze, prev_country = country_list[id-1]
    cur_gold, cur_silver, cur_bronze, cur_country = country_list[id]

    if not (prev_gold == cur_gold and prev_silver == cur_silver and prev_bronze == cur_bronze):
        rank += acc
        acc = 1
    else:
        acc += 1
    country_rank[cur_country] = rank

print(country_rank[country_num])
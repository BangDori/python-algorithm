import sys
input = sys.stdin.readline

# 접시의 수, 초밥의 수, 연속해서 먹는 접시의 수, 쿠폰 번호
dishes, sushi_count, continuous_count, coupon = map(int, input().split())
sushi_list = []
for _ in range(dishes):
    sushi_list.append(int(input().rstrip()))

slice_count = continuous_count
sushi_list += sushi_list[:-1]

sushi_dict = {}

for s in sushi_list[:slice_count]:
    if not sushi_dict.get(s):
        sushi_dict[s] = 0
    sushi_dict[s] += 1
sushi_dict[coupon] = dishes+1

# 먹을 수 있는 초밥의 가짓수의 최댓값
max_dishes_count = len(sushi_dict.keys())
for idx in range(slice_count, dishes*2-1):
    if not sushi_dict.get(sushi_list[idx]):
        sushi_dict[sushi_list[idx]] = 0
    sushi_dict[sushi_list[idx]] += 1

    sushi_dict[sushi_list[idx-slice_count]] -= 1
    if sushi_dict[sushi_list[idx-slice_count]] == 0:
        sushi_dict.pop(sushi_list[idx-slice_count])

    max_dishes_count = max(max_dishes_count, len(sushi_dict.keys()))

print(max_dishes_count)
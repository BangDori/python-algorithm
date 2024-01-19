# 사람의 수
N = int(input())
people = []
rank = [1 for _ in range(N)]

for _ in range(N):
    height, weight = map(int, input().split())
    people.append((height, weight))

count = 0
for weight_x, height_x in people:
    for weight_y, height_y in people:
        if weight_x < weight_y and height_x < height_y:
            rank[count] += 1
    
    count += 1

for ranking in rank:
    print(ranking, end=' ')
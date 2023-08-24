# 사람의 수
N = int(input())
people = []
rank = [0 for _ in range(N)]

for _ in range(N):
    # 몸무게 (x), 키 (y)
    x, y = map(int, input().split())
    people.append((x, y))

count = 0
for weight_a, height_a in people:
    for weight_b, height_b in people:
        if weight_a < weight_b and height_a < height_b:
            rank[count] += 1
    
    count += 1

for ranking in rank:
    print(ranking + 1, end=' ')
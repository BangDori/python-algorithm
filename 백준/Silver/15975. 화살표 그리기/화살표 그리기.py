# import sys
# input = sys.stdin.readline

# M = int(input())
# heights = list(map(int, input().split()))

# # 직전 연주 음 < 현재 연주 음 => 직전에 쓴 수보다 큰 수 추가
# # 직전 연주 음 > 현재 연주 음 => 직전에 쓴 수보다 작은 수 추가
# # 직전 연주 음 = 현재 연주 음 => 직전에 쓴 수 추가

# current = heights.pop()
# heights.reverse()

# array = [1,]
# count = 1
# for height in heights:
#     if current < height:
#         count += 1
#     elif current > height:
#         count = 1
    
#     array.append(count)
#     current = height

# print(max(array))

import sys
input = sys.stdin.readline

N = int(input())

matrix = {}

for _ in range(N):
    pos, color = map(int, input().split())
    
    if not matrix.get(color):
        matrix[color] = []    
    matrix[color].append(pos)

for key in matrix.keys():
    if len(matrix[key]) == 1:
        continue

    matrix[key].sort()

answer = 0
for coords in matrix.values():
    if len(coords) == 1:
        continue

    for i in range(len(coords)):
        min_diff = float('inf')

        if i-1 >= 0:
            min_diff = abs(coords[i]-coords[i-1])
        
        if i+1 < len(coords):
            min_diff = min(min_diff, abs(coords[i]-coords[i+1]))
        
        answer += min_diff

print(answer)
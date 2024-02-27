dr = [1, 0, -1]
dc = [0, 1, -1]

def solution(n):
    triangle = [[0] * i for i in range(1, n+1)] 
    r, c, number = -1, 0, 1

    for i in range(n):
        for _ in range(i, n):
            r += dr[i%3]
            c += dc[i%3]
            
            triangle[r][c] = number
            number += 1
    
    answer = []
    for line in triangle:
        answer += line

    return answer

# 1 => 1
# 2 => 3
# 3 => 6
# 4 => 10

#         1
#        2  9
#       3 10 8
#      4 5  6 7

#         0
#        1 2
#       3 4 5
#      6 7 8 9
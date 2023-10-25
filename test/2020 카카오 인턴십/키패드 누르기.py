from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def get_distance(keywords, find_number, cur):
    visited = [[False] * len(keywords[0]) for _ in range(len(keywords))]
    cur_x, cur_y = cur
    
    queue = deque([(cur_x, cur_y, 0)])
    while queue:
        x, y, count = queue.popleft()
        
        if keywords[x][y] == find_number:
            return count
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < 4 and 0 <= ny < 3 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, count+1))

    return -1
                

def solution(numbers, hand):    
    keywords = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]    
    answer = ''
    cur_left = (3, 0)
    cur_right = (3, 2)
    
    for number in numbers:        
        if number in [1, 4, 7]:
            answer += 'L'
            cur_left = ((number-1)//3, 0)
            continue
        
        if number in [3, 6, 9]:
            answer += 'R'
            cur_right = (number//3-1, 2)
            continue
            
        left_distance = get_distance(keywords, number, cur_left)
        right_distance = get_distance(keywords, number, cur_right)
        
        if left_distance < right_distance:
            answer += 'L'
            if number == 0:
                cur_left = (3, 1)
            else:
                cur_left = (number//3, 1)
        if right_distance < left_distance:
            answer += 'R'
            if number == 0:
                cur_right = (3, 1)
            else:
                cur_right = (number//3, 1)
        
        if left_distance == right_distance:
            if hand == 'right':
                answer += 'R'
                if number == 0:
                    cur_right = (3, 1)
                else:
                    cur_right = (number//3, 1)
            else:
                answer += 'L'
                if number == 0:
                    cur_left = (3, 1)
                else:
                    cur_left = (number//3, 1)

    return answer
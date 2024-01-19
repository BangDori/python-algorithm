import sys
input = sys.stdin.readline

def moveCloud(cloud, dir, dist):
    moved_cloud = []

    for y, x in cloud:
        ny = (y + dy[dir] * dist) % size
        nx = (x + dx[dir] * dist) % size

        board[ny][nx] += 1
        moved_cloud.append((ny, nx))
    
    return moved_cloud

def rainCloud(moved_cloud):
    for y, x in moved_cloud:
        count = 0

        for i in range(2, 9, 2):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < size and 0 <= nx < size and board[ny][nx] > 0:
                count += 1
        
        board[y][x] += count

def cleanupCloud(moved_cloud):
    new_cloud = []

    for y in range(size):
        for x in range(size):
            if (y, x) in moved_cloud or board[y][x] < 2:
                continue

            board[y][x] -= 2
            new_cloud.append((y, x))
    
    return new_cloud
    
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1] # y축
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1] # x축

size, command_count = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(size)]
command = [map(int, input().split()) for _ in range(command_count)]

# y, x
cloud = [(size-1, 0), (size-1, 1), (size-2, 0), (size-2, 1)]
for dir, dist in command:
    moved_cloud = moveCloud(cloud, dir, dist)
    rainCloud(moved_cloud)
    cloud = cleanupCloud(moved_cloud)

answer = 0
for i in range(size):
    answer += sum(board[i])
print(answer)
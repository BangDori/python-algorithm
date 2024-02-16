from heapq import heappush, heappop
import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

SIZE = int(input())
board = [list(map(int, input().split())) for _ in range(SIZE)]
slope = [[1e9] * SIZE for _ in range(SIZE)]

def dijkstra():
    min_diff = 1e9

    # slope_diff, row, col
    heap = [(0, 0, 0)]
    slope[0][0] = 0

    while heap:
        diff, row, col = heappop(heap)

        if row == SIZE-1 and col == SIZE-1:
            min_diff = min(min_diff, diff)
            break

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            if 0 <= nr < SIZE and 0 <= nc < SIZE and slope[nr][nc] > abs(board[nr][nc] - board[row][col]):
                slope[nr][nc] = abs(board[nr][nc] - board[row][col])
                heappush(heap, (max(diff, abs(board[nr][nc] - board[row][col])), nr, nc))

    return min_diff

answer = dijkstra()
print(answer)
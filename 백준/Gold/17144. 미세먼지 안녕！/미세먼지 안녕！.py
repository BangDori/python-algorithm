import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

R, C, T = map(int, input().split())
dust = [[0] * C for _ in range(R)]
room = [list(map(int, input().split())) for _ in range(R)]
cleaner = 2

for r in range(2, R):
    if room[r][0] == -1:
        cleaner = r
        break

def expand_dust():
    for r in range(R):
        for c in range(C):
            if room[r][c] == -1:
                dust[r][c] = -1
                continue

            count = 0
            for i in range(4):
                nr = r + dy[i]
                nc = c + dx[i]

                if 0 <= nr < R and 0 <= nc < C and room[nr][nc] != -1:
                    dust[nr][nc] += room[r][c] // 5
                    count += 1
                    # room[r][c] = dust[nr][nc]
            dust[r][c] += room[r][c] - (room[r][c]//5)*count

def diffusion_dust():
    for r in range(cleaner-1, -1, -1):
        dust[r][0] = dust[r-1][0]
    for r in range(cleaner+2, R-1):
        dust[r][0] = dust[r+1][0]

    for c in range(C-1):
        dust[0][c] = dust[0][c+1]
        dust[-1][c] = dust[-1][c+1]

    for r in range(cleaner):
        dust[r][C-1] = dust[r+1][C-1]
    for r in range(R-1, cleaner, -1):
        dust[r][C-1] = dust[r-1][C-1]

    for c in range(C-1):
        dust[cleaner][(C-1)-c] = dust[cleaner][(C-1)-(c+1)]
        dust[cleaner+1][(C-1)-c] = dust[cleaner+1][(C-1)-(c+1)]
    dust[cleaner][1] = dust[cleaner+1][1] = 0

while T > 0:
    # 미세먼지 확장
    expand_dust()

    # 공기청정기 바람 ↓ ← ↑ →
    diffusion_dust()
    room = [[dust[r][c] for c in range(C)] for r in range(R)]
    dust = [[0 for _ in range(C)] for _ in range(R)]

    T -= 1

answer = 0
for r in range(R):
    for c in range(C):
        if room[r][c] == -1: continue
        answer += room[r][c]

print(answer)
"""
    2 sec, 512 MB

    축구를 하기 위해 모인 사람은 총 N명 (N은 짝수)

    N / 2 명으로 이루어진 스타트 팀과 링크 팀

    번호 1 ~ N (4 <= N <= 20)

    S(ij)는 i번 + j번 시너지

    이렇게 팀을 꾸렸을 때, 팀 능력치의 차이가 최소

    # 01, 02, 03, 12, 13, 23 이 되게 해야함
    # 23, 13, 12, 03, 02, 01
"""

import sys, itertools
input = sys.stdin.readline

N = int(input())
players = [i for i in range(N)]
nCr = list(itertools.combinations(players, N // 2))
teams = [list(map(int, input().split())) for _ in range(N)]

min_diff = sys.maxsize

for k in range(len(nCr)):
    sum_start = 0
    sum_link = 0
    start_players_list = list(itertools.combinations(nCr[k], 2))
    link_players_list = list(itertools.combinations(nCr[len(nCr) - 1 - k], 2))

    for player in start_players_list:
        sum_start += (teams[player[0]][player[1]] + teams[player[1]][player[0]])

    for player in link_players_list:
        sum_link += (teams[player[0]][player[1]] + teams[player[1]][player[0]])
    
    if abs(sum_start - sum_link) <= min_diff:
        min_diff = abs(sum_start - sum_link)

print(min_diff)
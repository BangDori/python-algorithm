# 참고
# https://velog.io/@peacemiller/백준-3758-KCPC-python

import sys
input = sys.stdin.readline

test_case = int(input().rstrip())

for _ in range(test_case):
    # 팀의 수, 문제의 수, 아이디, 로그 기록의 수
    teams, problems, my_id, logs = map(int, input().split())

    score_list = [[0 for _ in range(problems)] for _ in range(teams)]
    submit_list = [0 for _ in range(teams)]
    log_list = [0 for _ in range(teams)] 

    for log in range(logs):
        team_id, problem_id, score = map(int, input().rstrip().split())
        score_list[team_id-1][problem_id-1] = max(score_list[team_id-1][problem_id-1], score)
        submit_list[team_id-1] += 1
        log_list[team_id-1] = log

    total_board = []
    for team in range(teams):
        total_board.append((sum(score_list[team]), submit_list[team], log_list[team], team+1))
    
    total_board.sort(key=lambda x: (-x[0], x[1], x[2]))

    for rank in range(len(total_board)):
        if total_board[rank][3] == my_id:
            print(rank+1)
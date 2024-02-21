import sys
input = sys.stdin.readline

GAME_TIME = 48 * 60

def convertTimeToNumber(time):
    min, sec = map(int, time.split(":"))
    goalTime = min * 60 + sec

    return goalTime

def convertNumberToTime(number):
    time = [str(int(number // 60)).zfill(2), str(int(number % 60)).zfill(2)]
    return ":".join(time)

goal_cnt = int(input())
scoreBoard = {}

for i in range(goal_cnt):
    tid, time = list(input().strip().split())
    goalTime = convertTimeToNumber(time)
    scoreBoard[goalTime] = int(tid)

team1_goalCnt = 0; team2_goalCnt = 0
team1_winTime = 0; team2_winTime = 0

for time in range(GAME_TIME+1):
    if team1_goalCnt > team2_goalCnt: team1_winTime += 1
    elif team1_goalCnt < team2_goalCnt: team2_winTime += 1

    if scoreBoard.get(time):
        tid = scoreBoard.get(time)

        if tid == 1: team1_goalCnt += 1
        else: team2_goalCnt += 1

team1_answer = convertNumberToTime(team1_winTime)
team2_answer = convertNumberToTime(team2_winTime)

print(team1_answer, team2_answer, sep='\n')
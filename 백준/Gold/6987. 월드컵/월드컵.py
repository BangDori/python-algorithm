def is_error_game(result):
    for team in result:
        if sum(team) != 5:
            return True
    
    return False

def is_enable_result(result):
    for team in result:
        if team != [0, 0, 0]:
            return 0

    return 1

def back_tracking(home, away):
    global game_result, enable
    
    if away == 6:
        home += 1
        away = home + 1
    
    if home == 5:
        if is_enable_result(game_result):
            enable = 1
        return

    # home 승리
    if game_result[home][0] > 0 and game_result[away][2] > 0:
        game_result[home][0], game_result[away][2] = game_result[home][0]-1, game_result[away][2]-1
        back_tracking(home, away+1)
        game_result[home][0], game_result[away][2] = game_result[home][0]+1, game_result[away][2]+1

    # home 무승부
    if game_result[home][1] > 0 and game_result[away][1] > 0:
        game_result[home][1], game_result[away][1] = game_result[home][1]-1, game_result[away][1]-1
        back_tracking(home, away+1)
        game_result[home][1], game_result[away][1] = game_result[home][1]+1, game_result[away][1]+1

    # home 패배
    if game_result[home][2] > 0 and game_result[away][0] > 0:
        game_result[home][2], game_result[away][0] = game_result[home][2]-1, game_result[away][0]-1
        back_tracking(home, away+1)
        game_result[home][2], game_result[away][0] = game_result[home][2]+1, game_result[away][0]+1

answer = []
for round in range(4):
    result = list(map(int, input().split()))
    game_result = []

    if is_error_game(game_result):
        answer.append(0)
        continue

    for i in range(0, len(result), 3):
        game_result.append(result[i:i+3])
    
    enable = 0
    back_tracking(0, 1)
    answer.append(enable)
    
print(*answer)
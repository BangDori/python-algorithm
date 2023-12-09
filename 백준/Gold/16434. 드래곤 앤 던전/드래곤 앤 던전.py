import sys
input = sys.stdin.readline    

room_count, atk = map(int, input().split())
room = []
for _ in range(room_count):
    t, a, h = map(int, input().split())
    room.append((t, a, h))

def play(minHP, maxHP, atk):
    answer = maxHP

    while minHP <= maxHP:
        HP = (minHP+maxHP)//2
        isClear = enterDongen(HP, atk)

        if isClear:
            answer = min(HP, answer)
            maxHP = HP - 1
        else:
            minHP = HP + 1
    
    return answer

def enterDongen(HP, atk):
    curHP = HP
    curATK = atk

    i = 0
    for t, a, h in room:
        i += 1
        if t == 1:
            if curATK >= h:
                continue

            # 전투
            user_atk_count = h // curATK
            if user_atk_count * curATK < h:
                user_atk_count += 1
            
            dragon_atk_count = user_atk_count - 1
            if dragon_atk_count * a >= curHP:
                return False

            curHP -= dragon_atk_count * a
            # print(i, "번째 방 전투 결과:", curHP)
            # print(i, "번째 공격 횟수:", user_atk_count, dragon_atk_count)
        elif t == 2:
            # 포션회복
            curATK += a
            curHP = min(curHP+h, HP)
    
    return True

answer = play(1, sys.maxsize, atk)
print(answer)
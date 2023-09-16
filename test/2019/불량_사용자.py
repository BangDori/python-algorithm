answer = []

def solution(user_id, banned_id):
    ban_list = []
    
    for idx, bid in enumerate(banned_id):
        ban_list.append([])
        for uid in user_id:
            if is_banned(uid, bid):
                ban_list[idx].append(uid)
                
    answer_list = [0 for _ in range(len(ban_list))]
    
    dfs(0, ban_list, answer_list)
    
    return len(answer)

def dfs(row, ban_list, answer_list):
    global answer
    if row == len(ban_list):
        copy_answer_list = answer_list.copy()
        copy_answer_list.sort()
        
        if copy_answer_list not in answer:
            answer.append(copy_answer_list)
        return
    
    for ban in ban_list[row]:
        if ban not in answer_list:
            answer_list[row] = ban
            dfs(row+1, ban_list, answer_list)
            answer_list[row] = -1
        
def is_banned(uid, bid):
    if len(uid) != len(bid):
        return False
    for c, b in zip(uid, bid):
        if b != '*' and c != b:
            return False
    return True
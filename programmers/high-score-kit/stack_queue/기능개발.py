def ceil(num):
    if num - int(num) > 0:
        return int(num) + 1
    else:
        return int(num)

def solution(progresses, speeds):
    # 7 3 9
    # 5 10 1 1 20 1
    remain_dates = []
    
    for idx, progress in enumerate(progresses):
        remain_date = ceil((100 - progress) / speeds[idx])
        remain_dates.append(remain_date)

    answer = []
    current = remain_dates[0]
    count = 0
    for remain in remain_dates:
        if remain <= current:
            count += 1
            continue
        
        answer.append(count)
        current = remain
        count = 1
    answer.append(count)
    
    return answer
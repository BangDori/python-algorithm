def round(size):
    if size - int(size) >= 0.5:
        return int(size) + 1
    else:
        return int(size)

def solution(nums):
    uniques_nums = list(set(nums))
    selected = round(len(nums) / 2)
    
    answer = 0
    if len(uniques_nums) > selected:
        answer = selected
    else:
        answer = len(uniques_nums)
    return answer
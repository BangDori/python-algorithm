def solution(gems):
    answer = [1, len(gems)]
    unique_gems = set(gems)
    gems_dict = {}

    for gem in unique_gems:
        gems_dict[gem] = 0

    left = 0
    right = 0
    gems_dict[gems[right]] = 1
    tot = 1
    
    while True:
        if tot >= len(unique_gems):
            if answer[1]-answer[0] > right-left:
                answer = [left+1, right+1]

        if gems_dict[gems[left]] > 1:
            gems_dict[gems[left]] -= 1
            left += 1
            continue

        if right < len(gems)-1:
            right += 1
            gems_dict[gems[right]] += 1
            if gems_dict[gems[right]] == 1:
                tot += 1
            continue

        break
    
    return answer
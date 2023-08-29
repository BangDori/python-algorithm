def solution(clothes):
    clothes_dict = {}
    
    answer = 0
    for cloth in clothes:
        if not clothes_dict.get(cloth[1]):
            clothes_dict[cloth[1]] = 1
        else:
            clothes_dict[cloth[1]] += 1
    
    tot = 1
    for value in clothes_dict.values():
        tot *= (value+1)
    answer = tot - 1
    
    return answer
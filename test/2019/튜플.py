def solution(s):
    answer = []
    formatted_s = s[1:-1]
    
    tuple_list = formatted_s.replace("},{", '|')
    tuple_list = tuple_list.replace('{', '').replace('}', '')
    tuple_list = tuple_list.split('|')
    
    for idx, tuple in enumerate(tuple_list):
        tuple_list[idx] = tuple.split(',')
    
    tuple_list.sort(key=lambda key: len(key))
    
    for tuple in tuple_list:
        for num in tuple:
            if answer.count(int(num)) > 0:
                continue
            answer.append(int(num))
    
    return answer
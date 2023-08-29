def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    answer.append(arr[0])
    
    cur = 0
    for i in range(1, len(arr)):
        if answer[cur] == arr[i]:
            continue
        
        cur += 1
        answer.append(arr[i])
        
    return answer
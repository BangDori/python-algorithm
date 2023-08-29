def solution(prices):
    answer = []
    
    for cur in range(len(prices)):
        timer = 0
        
        for next in range(cur+1, len(prices)):
            timer += 1

            if prices[cur] > prices[next]:
                break
        
        answer.append(timer)
        
    return answer
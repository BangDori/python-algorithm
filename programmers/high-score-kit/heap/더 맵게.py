import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    while True:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            answer = -1
            break
        second = heapq.heappop(scoville)
        new_scovil = first + second * 2
        heapq.heappush(scoville, new_scovil)
        answer += 1
    
    return answer
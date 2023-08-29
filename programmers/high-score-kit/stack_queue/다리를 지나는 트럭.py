from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    # 다리를 모두 건넌 트럭
    end_trucks = deque()    
    # 다리를 건너고 있는 트럭의 무게
    running_trucks = deque()
    # 다리를 건너고 있는 트럭의 현재 위치
    timer_trucks = deque()
    
    # 현재 다리 위에 있는 트럭
    current_truck = 0
    # 현재 다리 위의 무게
    current_weight = 0
    
    # 다리를 모두 건넌 트럭이 건너야 하는 트럭의 개수보다 적을때까지 
    while len(end_trucks) < len(truck_weights):
        answer += 1
        
        if current_truck != 0:
            # 트럭들 한 칸씩 전진
            for idx, timer in enumerate(timer_trucks):
                timer_trucks[idx] = timer + 1
            
            # 현재 다리를 건너는 트럭이 있다면
            if timer_trucks[0] >= bridge_length:
                # 첫번째 트럭의 위치가, 다리의 마지막 지점이라면
                current_weight -= running_trucks[0]
                end_trucks.append(running_trucks.popleft())
                timer_trucks.popleft()
            
        if current_truck < len(truck_weights):
            # 현재 다리 위에 있는 트럭이 마지막이 아니라면
            if current_weight + truck_weights[current_truck] <= weight:
                # 현재 무게와 다음번 트럭의 무게가 다리의 무게보다 작다면
                running_trucks.append(truck_weights[current_truck])
                timer_trucks.append(0)
                current_weight += truck_weights[current_truck]
                current_truck += 1
    
    return answer
# 트럭에 실을 수 있는 재활용 택배 상자의 최대 개수 cap
# 그리디인?

def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0
    
    current_delivery = 0
    current_pickup = 0
    
    for i in range(n):
        current_delivery += deliveries[i]
        current_pickup += pickups[i]
        
        while current_delivery > 0 or current_pickup > 0:
            current_delivery -= cap
            current_pickup -= cap
            
            answer += (n-i) * 2 # 이동거리
            
    return answer
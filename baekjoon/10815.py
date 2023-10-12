# 숫자 카드의 수 (N)
N = int(input())
cards = list(map(int, input().split()))
card_map = {}

for i in range(N):
    card_map[cards[i]] = 1

# 확인 개수
M = int(input())
checks = list(map(int, input().split()))

for i in range(M):
    if card_map.get(checks[i]) == None:
        print(0, end=' ')
    else:
        print(card_map.get(checks[i]), end=' ')

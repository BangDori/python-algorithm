# 소유한 숫자 카드의 개수 (N)
N = int(input())
cards = list(map(int, input().split()))
cards_map = {}

for i in range(N):
    if cards_map.get(cards[i]) == None:
        cards_map[cards[i]] = 1
    else:
        cards_map[cards[i]] += 1

# 상근이가 몇 개 가지고 있는 숫자 카드 (M)
M = int(input())
quiz_cards = list(map(int, input().split()))

for i in range(M):
    if cards_map.get(quiz_cards[i]) == None:
        print(0, end=' ')
    else:
        print(cards_map.get(quiz_cards[i]), end=' ')
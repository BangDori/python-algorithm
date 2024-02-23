from heapq import heappush, heappop, heapify
import sys
input = sys.stdin.readline

cardCount, unionCount = map(int, input().split())
cards = list(map(int, input().split()))

heapify(cards)

for _ in range(unionCount):
    card1 = heappop(cards)
    card2 = heappop(cards)

    union_card = card1 + card2

    heappush(cards, union_card)
    heappush(cards, union_card)

print(sum(cards))
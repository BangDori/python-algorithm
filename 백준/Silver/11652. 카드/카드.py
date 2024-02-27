import sys
input = sys.stdin.readline

N = int(input())
card_dict = {}

for _ in range(N):
    number = int(input())

    if not card_dict.get(number):
        card_dict[number] = 0
    card_dict[number] += 1

cards = []
for number, count in zip(card_dict.keys(), card_dict.values()):
    cards.append((number, count))

cards.sort(key=lambda x: (-x[1], x[0]))
print(cards[0][0])
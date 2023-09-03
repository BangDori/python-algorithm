import sys
input = sys.stdin.readline

def binary_search(num):
    global answer
    min = 0
    max = len(cards) - 1

    while min <= max:
        mid = (min + max) // 2

        if cards[mid] == num:
            return cards_dict.get(cards[mid])
        elif cards[mid] < num:
            min = mid + 1
        else:
            max = mid - 1
    
    return 0

N = int(input())
cards = list(map(int, input().split()))
cards_dict = {}
for card in cards:
    if not cards_dict.get(card):
        cards_dict[card] = 1
    else:
        cards_dict[card] += 1
cards = list(set(cards))
cards.sort()

answer = 0

M = int(input())
finds = list(map(int, input().split()))

for find in finds:
    answer = binary_search(find)
    print(answer, end=' ')
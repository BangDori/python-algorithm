# Wrong Answer

from collections import deque
import sys
input = sys.stdin.readline

cards = int(input())

left_cards = deque(list(map(int, input().split())))
right_cards = deque(list(map(int, input().split())))

dp = [0]

# 규칙 3 카드가 남지 않을 때까지 반복
while left_cards and right_cards:
    print(left_cards[0], right_cards[0])
    score = dp[-1]
    
    if left_cards[0] > right_cards[0]:
        # 규칙 2
        right_card = right_cards.popleft()
        dp.append(score + right_card)
    else:
        # 규칙 1
        if len(left_cards) > 1 and left_cards[1] > right_cards[0]:
            left_cards.popleft()
        else:
            right_cards.popleft()
            left_cards.popleft()

print(dp[-1])